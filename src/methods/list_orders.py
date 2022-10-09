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

    return jsonify(
        {
            'status': 'ok',
            'orders': orders,
        }
    )
