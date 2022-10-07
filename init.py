import secrets

import bcrypt

from src.config import POSTGRESQL_CONNECTION_PARAMS
from src.utils.exequte_sql import execute_sql


execute_sql(
    'DROP TABLE IF EXISTS users, commands, achievements, products ',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)
execute_sql(
    'CREATE TABLE users('
    'id SERIAL PRIMARY KEY, '
    'token VARCHAR NOT NULL, '
    'hash_and_salt VARCHAR NOT NULL, '
    'photo_url VARCHAR NOT NULL, '
    'first_name VARCHAR NOT NULL, '
    'middle_name VARCHAR NOT NULL, '
    'last_name VARCHAR NOT NULL, '
    'email VARCHAR NOT NULL, '
    'phone VARCHAR NOT NULL, '
    'team_id INTEGER NOT NULL, '
    'job VARCHAR NOT NULL, '  # example: senior flutter developer
    'rights INTEGER NOT NULL, '  # 1 - simple user, 2 - admin, 3 - manager, 4 - editor
    'coins INTEGER NOT NULL, '
    'thanksgivings INTEGER NOT NULL, '
    'address VARCHAR NOT NULL, '
    'achievements INTEGER[] NOT NULL, '
    'cart JSONB NOT NULL'
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
    'title VARCHAR NOT NULL, '
    'price INTEGER NOT NULL, '
    'description VARCHAR NOT NULL, '
    'photo_links VARCHAR[] NOT NULL'
    ')',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)
execute_sql(
    'CREATE TABLE achievements('
    'id SERIAL PRIMARY KEY, '
    'title VARCHAR NOT NULL, '
    'description VARCHAR NOT NULL, '
    'people_gets_count INTEGER NOT NULL, '
    'price INTEGER NOT NULL, '
    'photo_links VARCHAR[] NOT NULL'
    ')',
    (),
    POSTGRESQL_CONNECTION_PARAMS,
)