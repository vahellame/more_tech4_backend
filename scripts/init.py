import secrets

import bcrypt

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


execute_sql(
    'DROP TABLE IF EXISTS users, teams, achivments, products ',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)
execute_sql(
    'CREATE TABLE users('
    'id SERIAL PRIMARY KEY, '
    'token VARCHAR, '
    'public_key VARCHAR, '
    'hash_and_salt VARCHAR, '
    'first_name VARCHAR NOT NULL, '
    'middle_name VARCHAR NOT NULL, '
    'last_name VARCHAR NOT NULL, '
    'email VARCHAR NOT NULL, '
    'phone VARCHAR NOT NULL, '
    'team_id INTEGER NOT NULL, '
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
