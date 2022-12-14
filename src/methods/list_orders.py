from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_list_orders(request: Request):
    token = get_token_from_request(request)
    user_id = execute_sql(
        'SELECT id '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['id']
    orders = execute_sql(
        "SELECT * "
        "FROM orders "
        "WHERE user_id = %s",
        (user_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    orders_list = []
    for order in orders:
        old_cart = order['products']
        cart_list = []
        for product_id in order['products'].keys():
            product_id = int(product_id)
            product_data = execute_sql(
                'SELECT * '
                'FROM products '
                'WHERE id = %s',
                (product_id,),
                POSTGRESQL_CONNECTION_PARAMS,
            )[0]
            product_id = str(product_id)
            cart_list.append(
                {
                    'qty': old_cart[product_id],
                    'product_data': product_data,

                },
            )
        orders_list.append(cart_list)
    return jsonify(
        {
            'status': 'ok',
            'orders': orders_list,
        }
    )
