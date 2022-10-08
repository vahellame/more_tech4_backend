from flask import jsonify, Request
import requests

from src.config import POSTGRESQL_CONNECTION_PARAMS, CRYPTO_BASE_URL
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request

def process_whoami(request: Request):
    token = get_token_from_request(request)
    user_data = execute_sql(
        'SELECT * '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    public_key = execute_sql(
        'SELECT public_key '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )

    balance = requests.get(
        f'{CRYPTO_BASE_URL}/v1/wallets/{public_key}/balance',
    )

    if len(user_data) != 0:
        response_dict = {
            'status': 'ok',
            'user': user_data[0],
            'balance': balance
        }
        return jsonify(response_dict)
    response_dict = {
        'status': 'error',
        'error': 'Пользователь не найден',
    }

    return jsonify(response_dict)
