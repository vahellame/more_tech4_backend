from flask import Request, jsonify


from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql

def process_search_user(request: Request):
    data = request.get_json()
    if 'email' in list(data.keys()):
        email = data['email']
        user_data = execute_sql(
            'SELECT * '
            'FROM users '
            'WHERE email = %s',
            (email,),
            POSTGRESQL_CONNECTION_PARAMS,
        )
    elif 'name' in list(data.keys()):
        name = data['name']
        name = f'%s{name}%s'
        user_data = execute_sql(
            'SELECT * ' 
            'FROM users ' 
            'WHERE first_name = %s OR middle_name = %s OR last_name = %s',
            (name,),
            POSTGRESQL_CONNECTION_PARAMS,
        )
    return jsonify(user_data)