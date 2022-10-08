from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_list_thanksgivings(request: Request):
    user_id = request.get_json()['user_id']
    list_thanksgivings = execute_sql(
        'SELECT thanksgivings '
        'FROM users '
        'WHERE user_id = %s',
        (user_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify(list_thanksgivings)