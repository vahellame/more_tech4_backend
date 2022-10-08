from flask import send_from_directory

from src.config import FILES_DIR_PATH


def process_photo(url: str):
    return send_from_directory(directory=FILES_DIR_PATH, path=url)
