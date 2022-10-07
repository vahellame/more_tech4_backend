# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS

from src.methods.login import process_login

app = Flask(__name__)
CORS(app)


@app.route("/login", methods=['POST'])
def handle_login():
    return process_login(request)

# [Unit]
#
# Description=FinArbitr Server
#
# [Service]
#
# Type=oheshot
# WorkingDirectory=/home/fa/finarbitr/backend
# ExecStart=/usr/sbin/runuser -l fa -c '/home/fa/finarbitr/backend/venv/bin/gunicorn --chdir /home/fa/finarbitr/backend app:app -b 0.0.0.0:8080 --threads=1 --workers=4 --reload'
#
# [Install]
#
# WantedBy=multi-user.target

# [Unit]
#
# Description=FinArbitr Server
#
# [Service]
#
# Type=oheshot
#
# ExecStart=/home/fa/finarbitr/autodeploy/venv/bin/python /home/fa/finarbitr/autodeploy/main.py
#
# [Install]
#
# WantedBy=multi-user.target


@app.route("/test", methods=['GET', 'POST'])
def handle_test():
    return jsonify(
        {
            'test': "Тест",
        }
    )
