from flask import send_file

from src.config import FILES_DIR_PATH


def process_photo(photo_path):
    return send_file(FILES_DIR_PATH + '/' + photo_path)
