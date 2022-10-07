from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_whoami(request: Request):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        token = ''
    user_data = execute_sql(
        'SELECT * '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )

    if len(user_data) != 0:
        response_dict = {
            'status': 'ok',
            'user': user_data[0]
        }
        return jsonify(response_dict)
    response_dict = {
        'status': 'error',
        'error': 'Пользователь не найден',
    }
    return jsonify(response_dict)
