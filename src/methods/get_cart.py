from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_get_cart(request: Request):
    token = get_token_from_request(request)
    cart = execute_sql(
        "SELECT cart "
        "FROM users "
        "WHERE token = %s",
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['cart']
    for product_id in cart.keys():
        product_id = int(product_id)
        product_data = execute_sql(
            'SELECT * '
            'FROM products '
            'WHERE id = %s',
            (product_id,),
            POSTGRESQL_CONNECTION_PARAMS,
        )[0]
        cart[product_id] = {
            'qty': cart[product_id],
            'product_data': product_data,
        }

    return jsonify(
        {
            'status': 'ok',
            'cart': cart,
        }
    )
