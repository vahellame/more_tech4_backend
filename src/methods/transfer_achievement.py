import time

import requests
from flask import Request, jsonify

from src.config import CRYPTO_BASE_URL, POSTGRESQL_CONNECTION_PARAMS, CRYPTO_OWNER_PRIVATE_KEY, BACKEND_BASE_URL, CRYPTO_OWNER_PUBLIC_KEY
from src.utils.exequte_sql import execute_sql


def process_transfer_achievement(request: Request):
    data = request.get_json()
    achievement_id = data['achievement_id']
    user_id_to = data['user_id_to']

    user_to_public_key = execute_sql(
        'SELECT public_key '
        'FROM users '
        'WHERE id = %s',
        (user_id_to,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['public_key']
    photo_id = execute_sql(
        'SELECT * '
        'FROM achievements '
        'WHERE id = %s',
        (achievement_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['photo_id']
    r = requests.post(
        f'{CRYPTO_BASE_URL}/v1/nft/generate',
        {
            "toPublicKey": CRYPTO_OWNER_PUBLIC_KEY,
            'uri': f'{BACKEND_BASE_URL}/photo/{photo_id}',
            "nftCount": 1,
        },
    )
    transaction_hash = r.json()['transaction_hash']
    time.sleep(10)
    r = requests.get(
        f'{CRYPTO_BASE_URL}/v1/nft/generate/{transaction_hash}',
    )
    token_id = r.json()['tokens'][0]
    r = requests.post(
        f'{CRYPTO_BASE_URL}/v1/transfers/nft',
        json={
            "fromPrivateKey": CRYPTO_OWNER_PRIVATE_KEY,
            "toPublicKey": user_to_public_key,
            "tokenId": token_id,
        }
    )
    transaction_hash = r.json()['transaction_hash']
    execute_sql(
        'INSERT INTO transactions(tx_hash, tx_type, amount, user_id_from, user_id_to) '
        'VALUES (%s, %s, %s, %s, %s)',
        (transaction_hash, 3, token_id, 1, user_id_to),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify(
        {
            'status': 'ok',
        },
    )
