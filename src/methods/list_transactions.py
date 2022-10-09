from flask import Request, jsonify

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_list_transactions(request: Request):
    user_id = request.get_json()['user_id']
    list_transactions = execute_sql(
        'SELECT * '
        'FROM transactions '
        'WHERE user_id_to = %s ',
        (user_id,),
        POSTGRESQL_CONNECTION_PARAMS,
    )

    return jsonify({
        'transactions': list_transactions,
        'status': 'ok'
    })