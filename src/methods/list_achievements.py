from flask import Request, jsonify, abort

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql
from src.utils.get_token_from_request import get_token_from_request


def process_list_achievements(request: Request):
    user_id = request.get_json()['user_id']
    user_achievements_ids = execute_sql(
        'SELECT achievement_ids '
        'FROM users '
        'WHERE id = %s',
        (user_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )[0]['achievement_ids']
    achievements = []
    for achievement_id in user_achievements_ids:
        achievement = execute_sql(
            'SELECT * '
            'FROM achievements '
            'WHERE id = %s ',
            (achievement_id,),
            POSTGRESQL_CONNECTION_PARAMS,
        )
        achievements.append(achievement)
    response_dict = {
        'status': 'ok',
        'achievements': achievements
    }
    return jsonify(response_dict)
