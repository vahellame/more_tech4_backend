from flask import Request, jsonify, abort

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_list_coworkers(request: Request):
    token = get_token_from_request(request)
    user_data = execute_sql(
        'SELECT team_id '
        'FROM users '
        'WHERE token = %s',
        (token,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    if len(user_data) != 0:
        coworkers = execute_sql(
            'SELECT * '
            'FROM users '
            'WHERE team_id = %s',
            (user_data[0]['team_id'],),
            POSTGRESQL_CONNECTION_PARAMS
        )
        return jsonify(
            {
                'status': 'ok',
                'users': coworkers,
             }
        )
    abort(403)
