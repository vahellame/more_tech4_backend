from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_search_user(request: Request):
    data = request.get_json()
    if 'email' in list(data.keys()):
        email = data['email']
        email = f"%{email}%"
        users_data = execute_sql(
            'SELECT * '
            'FROM users '
            'WHERE email ILIKE %s',
            (email,),
            POSTGRESQL_CONNECTION_PARAMS,
        )
        response_dict = {
            'status': 'ok',
            'users': users_data,
        }
        return jsonify(response_dict)
    elif 'name' in list(data.keys()):
        name = data['name']
        name = f'%{name}%'
        users_data = execute_sql(
            'SELECT * '
            'FROM users '
            'WHERE first_name ILIKE %s OR middle_name ILIKE %s OR last_name ILIKE %s',
            (name, name, name),
            POSTGRESQL_CONNECTION_PARAMS,
        )
        response_dict = {
            'status': 'ok',
            'users': users_data,
        }
        return jsonify(response_dict)

    return jsonify(
        {
            'status': 'error',
            'error': 'Пользователь не найден',
        }
    )


