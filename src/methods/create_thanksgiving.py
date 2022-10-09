from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_create_thanksgiving(request: Request):
    token = get_token_from_request(request)
    data = request.get_json()
    user_id_to = data['user_id_to']
    price = data['price']
    title = data['price']
    user_id_from = execute_sql(
        'SELECT id '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['id']
    execute_sql(
        'INSERT INTO thanksgivings(price, user_id_from, user_id_to, title) '
        'VALUES (%s, %s, %s, %s)',
        (price, user_id_from, user_id_to, title,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    execute_sql(
        'UPDATE users '
        'SET thanksgivings = thanksgivings + 1 '
        'WHERE id = %s',
        (user_id_to,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify({
        'status': 'ok'
    })
