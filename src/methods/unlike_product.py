from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_unlike_product(request: Request):
    token = get_token_from_request(request)
    product_id = request.get_json()['product_id']
    list_liked_products = execute_sql(
        'SELECT liked_product_ids '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['liked_product_ids']
    list_liked_products.remove(product_id)
    execute_sql(
        'UPDATE users '
        'SET liked_product_ids = %s '
        'WHERE token = %s',
        (list_liked_products, token,),
        POSTGRESQL_CONNECTION_PARAMS,
        )
    return jsonify({
        'status': 'ok'
    })
