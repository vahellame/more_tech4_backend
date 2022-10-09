from flask import Request, jsonify
from psycopg2.extras import Json

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_add_product_to_cart(request: Request):
    data = request.get_json()
    product_id = str(data['product_id'])
    token = get_token_from_request(request)
    cart = execute_sql(
        "SELECT cart "
        "FROM users "
        "WHERE token = %s",
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['cart']
    if product_id in (cart.keys()):
        cart[product_id] = cart[product_id] + 1
    else:
        cart[product_id] = 1
    execute_sql(
        'UPDATE users '
        'SET cart = %s '
        'WHERE token = %s',
        (Json(cart), token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify(
        {
            'status': 'ok',
        }
    )
