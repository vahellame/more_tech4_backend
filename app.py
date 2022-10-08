# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS

from src.methods.create_achievement import process_create_achievement
from src.methods.list_coworkers import process_list_coworkers
from src.methods.login import process_login
from src.methods.photo import process_photo
from src.methods.search_team import process_search_team
from src.methods.search_user import process_search_user
from src.methods.transfer_matics import process_transfer_matics
from src.methods.transfer_rubles import process_transfer_rubles
from src.methods.upload_photo import process_upload_photo
from src.methods.who import process_who
from src.methods.whoami import process_whoami

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
CORS(app)


# @app.before_request
# def handle_chunking():
#     """
#     Sets the "wsgi.input_terminated" environment flag, thus enabling
#     Werkzeug to pass chunked requests as streams.  The gunicorn server
#     should set this, but it's not yet been implemented.
#     """
#
#     transfer_encoding = request.headers.get("Transfer-Encoding", None)
#     if transfer_encoding == u"chunked":
#         request.environ["wsgi.input_terminated"] = False

# @app.errorhandler(Exception)
# def handle(_):
#     return jsonify(
#         {
#             'status': 'error',
#             'error': "Ошибка сервера",
#         }
#     )


@app.route("/login", methods=['POST'])
def handle_login():
    return process_login(request)


@app.route("/who", methods=['POST'])
def handle_who():
    return process_who(request)


@app.route("/whoami", methods=['GET'])
def handle_whoami():
    return process_whoami(request)


@app.route("/search_user", methods=['POST'])
def handle_search_user():
    return process_search_user(request)


@app.route("/search_team", methods=['POST'])
def handle_search_team():
    return process_search_team(request)


@app.route("/list_coworkers", methods=['POST'])
def handle_list_coworkers():
    return process_list_coworkers(request)


@app.route("/photo/<path:photo_path>", methods=['GET'])
def handle_photo(photo_path):
    return process_photo(photo_path)


@app.route("/upload_photo", methods=['POST'])
def handle_upload_photo():
    return process_upload_photo(request)


@app.route("/transfer_rubles", methods=['POST'])
def handle_transfer_rubles():
    return process_transfer_rubles(request)


@app.route("/transfer_matics", methods=['POST'])
def handle_transfer_matics():
    return process_transfer_matics(request)


@app.route("/create_achievement", methods=['POST'])
def handle_create_achievement():
    return process_create_achievement(request)


@app.route("/test", methods=['GET'])
def handle_test():
    return jsonify({'status': 'ok'})
