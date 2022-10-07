# -*- coding: utf-8 -*-
from http.client import HTTPException

from flask import Flask, jsonify, request
from flask_cors import CORS

from src.methods.list_coworkers import process_list_coworkers
from src.methods.login import process_login
from src.methods.search_team import process_search_team
from src.methods.search_user import process_search_user
from src.methods.whoami import process_whoami

app = Flask(__name__)
CORS(app)


@app.errorhandler(Exception)
def handle(_):
    return jsonify(
        {
            'status': 'error',
            'error': "Ошибка сервера",
        }
    ), 200


@app.route("/login", methods=['POST'])
def handle_login():
    return process_login(request)


@app.route("/whoami", methods=['GET'])
def handle_whoami():
    return process_whoami(request)


@app.route("/search_user", methods=['POST'])
def handle_search_user():
    return process_search_user(request)


@app.route("/search_team", methods=['POST'])
def handle_search_team():
    return process_search_team(request)


@app.route("/list_coworkers", methods=['GET'])
def handle_list_coworkers():
    return process_list_coworkers(request)

