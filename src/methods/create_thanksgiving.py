from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_create_thanksgiving(request: Request):
    token = get_token_from_request(request)
    user_id_to = request.get_json()['user_id_to']
    price = request.get_json()['price']
    user_id_from = execute_sql(
        'SELECT id '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['id']
    execute_sql(
        'INSERT INTO thanksgivings(price, user_id_from, user_id_to) '
        'VALUES (%s, %s, %s)',
        (price, user_id_from, user_id_to,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    execute_sql(
        'UPDATE users '
        'SET thanksgivings = thanksgivings + 1 '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify({
        'status': 'ok'
    })