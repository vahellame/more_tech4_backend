from flask import Request, jsonify
from psycopg2.extras import Json

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_buy_cart(request: Request):
    token = get_token_from_request(request)
    res = execute_sql(
        'SELECT id, cart '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]
    cart = res['cart']
    user_id = res['id']
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
        (user_id, Json(cart),),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    execute_sql(
        'UPDATE users '
        'SET cart = %s '
        'WHERE id = %s',
        (Json({}), user_id,),
        POSTGRESQL_CONNECTION_PARAMS
    )
    return jsonify({
        'status': 'ok'
    })
