import pandas as pd
from loguru import logger
from pathlib import Path
# from detect_encoding import detect_encoding
# from detect_delimiter import detect_delimiter

logger.remove()
logger.add(
    "logs/app.log",
    rotation="5 MB",
    retention="10 days",
    compression="zip")

def smart_xls_loader(file: Path):
    # if Path(path).is_dir():
    #     for file in Path(path).rglob("*"):
    #         enc = detect_encoding(file)
            # logger.debug(f"{file} encoding is {enc}")

            # logger.info("delimiter detection process starting....")
            # sep = detect_delimiter(file, enc)
            # logger.debug(f"delimiter in csv file {file} is {sep}")

            df = pd.read_excel(file, engine="xlrd")
            # df = pd.read_excel(file, encoding=enc, sep=sep)
            logger.success(f"Reading .xls file {file} successfully")
            return df