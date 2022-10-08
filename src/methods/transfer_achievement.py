import requests
from flask import Request

from src.config import CRYPTO_BASE_URL, POSTGRESQL_CONNECTION_PARAMS, CRYPTO_OWNER_PRIVATE_KEY, BACKEND_BASE_URL
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
    achievement_uri = execute_sql(
        'SELECT * '
        'FROM achievements '
        'WHERE id = %s',
        (achievement_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['photo_id']
    requests.post(
        f'{CRYPTO_BASE_URL}/v1/nft/generate',
        {
            "toPublicKey": CRYPTO_OWNER_PUBLIC_KEY,
            'uri': f'{BACKEND_BASE_URL}/photo/{photo_id}.png',
            "nftCount": 1,
        },
    )
    r = requests.post(
        f'{CRYPTO_BASE_URL}/v1/transfers/nft',
        json={
            "fromPrivateKey": CRYPTO_OWNER_PRIVATE_KEY,
            "toPublicKey": user_to_public_key,
            "tokenId": 5
        }
    )
