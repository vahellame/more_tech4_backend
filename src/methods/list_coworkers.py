# -*- coding: utf-8 -*-

from flask import Request, jsonify, abort

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_list_coworkers(request: Request):
    user_id = request.get_json()['user_id']
    user_data = execute_sql(
        'SELECT team_id '
        'FROM users '
        'WHERE id = %s',
        (user_id,),
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
