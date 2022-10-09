from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_list_liked_products(request: Request):
    token = get_token_from_request(request)
    list_liked_products = execute_sql(
        'SELECT liked_product_ids '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['liked_product_ids']
    products = []
    for product_id in list_liked_products:
        product = execute_sql(
            'SELECT * '
            'FROM products '
            'WHERE id = %s',
            (product_id,),
            POSTGRESQL_CONNECTION_PARAMS,
        )[0]
        products.append(product)
    return jsonify({
        'products': products,
        'status': 'ok'
    })
