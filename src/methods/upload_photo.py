import os
import secrets

from PIL import Image
from flask import Request, jsonify

from src.config import PHOTOS_DIR_PATH


def process_upload_photo(request: Request):
    file = request.files['file']
    tmp_filename = secrets.token_hex() + file.filename
    photo_id = len(os.listdir(PHOTOS_DIR_PATH)) + 1
    # im = Image.open(tmp_filename)
    # im.save(f'{photo_id}.png')
    file.save(os.path.join(PHOTOS_DIR_PATH, tmp_filename))
    os.remove(tmp_filename)
    return jsonify(
        {
            'status': 'ok',
            'photo_id': photo_id,
        }
    )
