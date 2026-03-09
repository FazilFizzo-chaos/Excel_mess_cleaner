import chardet, sys
from loguru import logger

def detect_encoding(path):
    with open(path, "rb") as f:
        logger.info("encoding detection.....")
        enc = chardet.detect(f.read(100000))["encoding"]
    return enc