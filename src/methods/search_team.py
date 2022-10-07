from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_search_team(request: Request):
    data = request.get_json()
    team_title = data['team_title']
    team_title = f"%s{team_title}%s"
    teams = execute_sql(
        'SELECT * '
        'FROM teams '
        'WHERE title ILIKE %s',
        (team_title,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    for i in range(len(teams)):
        team_id = teams[i]['id']
        team_users = execute_sql(
            'SELECT * '
            'FROM users '
            'WHERE team_id = %s',
            (team_id,),
            POSTGRESQL_CONNECTION_PARAMS,
        )
        teams[i]['users'] = team_users
    response_dict = {
        'status': 'ok',
        'teams': teams,
    }
    return jsonify(response_dict)
