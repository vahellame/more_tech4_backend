# -*- coding: utf-8 -*-
import requests
from flask import Request, jsonify

from src.config import CRYPTO_OWNER_PUBLIC_KEY, BACKEND_BASE_URL, CRYPTO_BASE_URL, POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_create_achievement(request: Request):
    data = request.get_json()
    title = data['title']
    description = data['description']
    price = data['price']
    photo_id = data['photo_id']
    # requests.post(
    #     f'{CRYPTO_BASE_URL}/v1/nft/generate',
    #     {
    #         "toPublicKey": CRYPTO_OWNER_PUBLIC_KEY,
    #         'uri': f'{BACKEND_BASE_URL}/photo/{photo_id}',
    #         "nftCount": 1,
    #     },
    # )
    execute_sql(
        "INSERT INTO achievements(title, description, people_gets_count, price, photo_id) "
        "VALUES (%s, %s, %s, %s, %s)",
        (title, description, 0, price, photo_id),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify(
        {'status': 'ok'}
    )
