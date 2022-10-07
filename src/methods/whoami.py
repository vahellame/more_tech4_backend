from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_whoami(request: Request):
    data = request.get_json()
    user_id = data['id']
    user_data = execute_sql(
        'SELECT * '
        'FROM users '
        'WHERE token = %s',
        (user_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify(user_data)