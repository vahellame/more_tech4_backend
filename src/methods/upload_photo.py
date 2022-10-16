import os
import secrets

from PIL import Image
from flask import Request, jsonify

from src.config import PHOTOS_DIR_PATH


def process_upload_photo(request: Request):
    file = request.files['file']
    #t0amp_filename = secrets.token_hex() + file.filename
    #file.save(file.filename)
    #photo_id = len(os.listdir(PHOTOS_DIR_PATH)) + 1
    #im = Image.open(tmp_filename)
    #im.save(f'{PHOTOS_DIR_PATH}/{photo_id}.png')
    # os.remove(tmp_filename)
    return jsonify(
        {
            'status': 'ok',
      #      'photo_id': f'{photo_id}.png',
        }
    )
