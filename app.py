# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS

from src.methods.login import process_login

app = Flask(__name__)
CORS(app)


@app.route("/login", methods=['POST'])
def handle_login():
    return process_login(request)


@app.route("/test", methods=['GET', 'POST'])
def handle_test():
    return jsonify(
        {
            'test': "Тест",
        }
    )