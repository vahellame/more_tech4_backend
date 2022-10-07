import secrets

import bcrypt

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql

# postgresql_connections_params_copy = POSTGRESQL_CONNECTION_PARAMS.copy()
#
# postgresql_connections_params_copy['dbname'] = 'postgres'

execute_sql(
    'DROP TABLE IF EXISTS users, commands, achivments, products ',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)
execute_sql(
    'CREATE TABLE users('
    'id SERIAL PRIMARY KEY, '
    'token VARCHAR, '
    'hash_and_salt VARCHAR, '
    'first_name VARCHAR NOT NULL, '
    'middle_name VARCHAR NOT NULL, '
    'last_name VARCHAR NOT NULL, '
    'email VARCHAR NOT NULL, '
    'phone VARCHAR NOT NULL, '
    'team_id INTEGER NOT NULL DEFAULT -1, '
    'coins INTEGER NOT NULL DEFAULT 0, '
    'address VARCHAR NOT NULL'
    ')',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)
execute_sql(
    'CREATE TABLE teams('
    'id SERIAL PRIMARY KEY, '
    'title VARCHAR, '
    'description VARCHAR, '
    'team_lead_id INTEGER '
    ')',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)
execute_sql(
    'CREATE TABLE products('
    'id SERIAL PRIMARY KEY, '
    'title VARCHAR, '
    'description VARCHAR, '
    'photo_links VARCHAR[] '
    ')',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)

token = secrets.token_hex(32)
hash_and_salt = bcrypt.hashpw('Cvb852456'.encode(encoding='utf-8'), bcrypt.gensalt()).decode(encoding='utf-8')
execute_sql(
    'INSERT INTO users('
    'token, '
    'hash_and_salt, '
    'first_name, '
    'middle_name, '
    'last_name, '
    'email, '
    'phone, '
    'command_id, '
    'coins, '
    'address'
    ') '
    'VALUES ('
    '%s, '
    '%s, '
    '%s, '
    '%s, '
    '%s, '
    '%s, '
    '%s, '
    '%s, '
    '%s, '
    '%s'
    ')',
    (
        token,
        hash_and_salt,
        'Илья',
        'Витальевич',
        'Николаев',
        'ilya@vtb.ru',
        '79772671124',
        1,
        0,
        'Москва',
    ),
    POSTGRESQL_CONNECTION_PARAMS
)