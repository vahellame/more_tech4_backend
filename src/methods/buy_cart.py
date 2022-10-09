from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_buy_cart(request: Request):
    token = get_token_from_request(request)
    user_id = execute_sql(
        'SELECT id '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['id']
    cart = execute_sql(
        'SELECT cart '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['cart']
    execute_sql(
        'UPDATE users '
        'SET cart = %s '
        'WHERE token = %s ',
        ({}, token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    execute_sql(
        'INSERT INTO orders(user_id, products) '
        'VALUES (%s, %s)',
        (user_id, cart,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify({
        'status': 'ok'
    })