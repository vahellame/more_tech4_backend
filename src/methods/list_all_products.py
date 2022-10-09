from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_list_all_products():
    products = execute_sql(
        'SELECT * '
        'FROM products ',
        (),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify(
        {
            'status': 'ok',
            'products': products,
        }
    )
