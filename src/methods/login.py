import bcrypt
from flask import jsonify, Request

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


def process_login(request: Request):
    data = request.get_json()
    login = data['login']
    maybe_phone = login
    maybe_phone = maybe_phone.replace('+', '')
    maybe_phone = maybe_phone.replace('-', '')
    maybe_phone = maybe_phone.replace(' ', '')
    maybe_phone = maybe_phone.replace('(', '')
    maybe_phone = maybe_phone.replace(')', '')
    if maybe_phone[0] == '8':
        # TODO: replace this
        maybe_phone = maybe_phone[1:]
        maybe_phone = '7' + maybe_phone
    password = data['password']
    res = execute_sql(
        f"SELECT * "
        f"FROM users "
        f"WHERE phone = %s OR email = %s",
        (maybe_phone, login,),
        POSTGRESQL_CONNECTION_PARAMS,
    )
    if len(res) == 0:
        response_dict = {
            'status': 'error',
            'error': "Телефон или email не зарегистрирован"
        }
        return jsonify(response_dict)

    hash_and_salt = res[0]['hash_and_salt']
    if bcrypt.checkpw(password.encode(encoding='utf-8'), hash_and_salt.encode(encoding='utf-8')) is not True:
        response_dict = {
            'status': 'ko',
            'error': 'Неправильный пароль',
        }
        return jsonify(response_dict)

    response_dict = {
        'status': 'ok',
        'user': res[0],
    }
    return jsonify(response_dict)
