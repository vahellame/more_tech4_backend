from flask import Request, jsonify
from psycopg2.extras import Json

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_remove_product_from_cart(request: Request):
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
    if cart[product_id] == 1:
        del cart[product_id]
    else:
        cart[product_id] = cart[product_id] - 1
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
