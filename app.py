# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS

from src.methods.login import process_login
from src.methods.search_team import process_search_team
from src.methods.search_user import process_search_user
from src.methods.whoami import process_whoami

app = Flask(__name__)
CORS(app)


@app.route("/login", methods=['POST'])
def handle_login():
    return process_login(request)


@app.route("/whoami", methods=['POST'])
def handle_whoami():
    return process_whoami(request)


@app.route("/search_user", methods=['POST'])
def handle_search_user():
    return process_search_user(request)


@app.route("/search_team", methods=['POST'])
def handle_search_team():
    return process_search_team(request)


@app.route("/test", methods=['GET', 'POST'])
def handle_test():
    return jsonify(
        {
            'test': "Тест",
        }
    )
