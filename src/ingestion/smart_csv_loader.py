import pandas as pd
from loguru import logger
from pathlib import Path
from src.ingestion.detect_encoding import detect_encoding
from src.ingestion.detect_delimiter import detect_delimiter

logger.remove()
logger.add(
    "logs/app.log",
    rotation="5 MB",
    retention="10 days",
    compression="zip")

def smart_csv_loader(file: Path):
    # if Path(path).is_dir():
    #     for file in Path(path).rglob("*"):
            enc = detect_encoding(file)
            logger.debug(f"{file} encoding is {enc}")

            logger.info("delimiter detection process starting....")
            sep = detect_delimiter(file, enc)
            logger.debug(f"delimiter in csv file {file} is {sep}")


            df = pd.read_csv(file, encoding=enc, sep=sep, on_bad_lines="skip")
            logger.success(f"Reading csv file {file} successfully")
            return df
    # if Path(path).is_file():
    #     enc = detect_encoding(Path(path))
    #     logger.debug(f"{path} encoding is {enc}")
    #
    #     logger.info("delimiter detection process starting....")
    #     sep = detect_delimiter(path, enc)
    #     logger.debug(f"delimiter in csv file {path} is {sep}")
    #
    #     df = pd.read_csv(path, encoding=enc, sep=sep, on_bad_lines="skip")
# smart_csv_loader("D:\\PythonProject\\input")