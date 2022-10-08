import os

from flask import Request, jsonify

from src.config import PHOTOS_DIR_PATH


def process_upload_photo(request: Request):
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(PHOTOS_DIR_PATH, filename))
    return jsonify(
        {'status': 'ok'}
    )
