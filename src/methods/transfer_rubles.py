import requests
from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS, CRYPTO_BASE_URL
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_transfer_rubles(request: Request):
    data = request.get_json()
    token = get_token_from_request(request)
    private_key_from = data['private_key_from']
    user_id_to = data['user_id_to']
    amount = data['amount']

    to_public_key = execute_sql(
        'SELECT public_key '
        'FROM users '
        'WHERE id = %s',
        (user_id_to,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['public_key']
    user_id_from = execute_sql(
        'SELECT id '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['id']
    response = requests.post(
        f'{CRYPTO_BASE_URL}/v1/transfers/ruble',
        json={
            "fromPrivateKey": private_key_from,
            "toPublicKey": to_public_key,
            "amount": amount
        }
    )
    transaction_hash = response.json()['transaction']
    execute_sql(
        'INSERT INTO transactions(tx_hash, tx_type, amount, user_id_from, user_id_to) '
        'VALUES (%s, %s, %s, %s, %s)',
        (transaction_hash, 1, amount, user_id_from, user_id_to),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify({'status': 'ok'})
