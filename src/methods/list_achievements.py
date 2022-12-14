import requests
from flask import Request, jsonify, abort

from src.config import POSTGRESQL_CONNECTION_PARAMS, CRYPTO_BASE_URL
from src.utils.exequte_sql import execute_sql


def process_list_achievements(request: Request):
    user_id = request.get_json()['user_id']
    user_achievements = execute_sql(
        'SELECT * '
        'FROM transactions '
        'WHERE tx_type = %s AND user_id_to = %s',
        (3, user_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    for i in range(len(user_achievements)):
        token_id = user_achievements[i]['amount']
        achievement_id = user_achievements[i]['achievement_id']
        r = requests.get(
            f"{CRYPTO_BASE_URL}/v1/nft/{token_id}"
        )
        user_achievements[i]['nft_data'] = r.json()
        achievement = execute_sql(
            "SELECT * "
            "FROM achievements "
            "WHERE id = %s",
            (achievement_id,),
            POSTGRESQL_CONNECTION_PARAMS,
        )[0]
        user_achievements[i]['user_achievement_data'] = achievement

    return jsonify(user_achievements)
