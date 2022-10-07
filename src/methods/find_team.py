from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql

def find_team(request: Request):
    data = request.get_json()
    email = data['email']
    team = execute_sql(
        'SELECT * '
        'FROM users '
        'WHERE email = %s',
        (email,),
        POSTGRESQL_CONNECTION_PARAMS,
    )