from flask import jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_list_all_achievements():
    all_achievements = execute_sql(
        'SELECT * '
        'FROM achievements ',
        (),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    return jsonify(all_achievements)
