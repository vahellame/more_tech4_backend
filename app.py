# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS

from src.methods.add_product_to_cart import process_add_product_to_cart
from src.methods.buy_cart import process_buy_cart
from src.methods.create_achievement import process_create_achievement
from src.methods.create_thanksgiving import process_create_thanksgiving
from src.methods.get_cart import process_get_cart
from src.methods.like_product import process_like_product
from src.methods.list_achievements import process_list_achievements
from src.methods.list_all_achievements import process_list_all_achievements
from src.methods.list_all_products import process_list_all_products
from src.methods.list_coworkers import process_list_coworkers
from src.methods.list_liked_products import process_list_liked_products
from src.methods.list_orders import process_list_orders
from src.methods.list_thanksgivings import process_list_thanksgivings
from src.methods.login import process_login
from src.methods.photo import process_photo
from src.methods.remove_product_from_cart import process_remove_product_from_cart
from src.methods.search_team import process_search_team
from src.methods.search_user import process_search_user
from src.methods.transfer_achievement import process_transfer_achievement
from src.methods.transfer_matics import process_transfer_matics
from src.methods.transfer_rubles import process_transfer_rubles
from src.methods.unlike_product import process_unlike_product
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

@app.errorhandler(Exception)
def handle(_):
    return jsonify(
        {
            'status': 'error',
            'error': "Ошибка сервера",
        }
    )


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


@app.route("/transfer_achievement", methods=['POST'])
def handle_transfer_achievement():
    return process_transfer_achievement(request)


@app.route("/list_achievements", methods=['POST'])
def handle_list_achievements():
    return process_list_achievements(request)


@app.route("/add_product_to_cart", methods=['POST'])
def handle_add_product_to_cart():
    return process_add_product_to_cart(request)


@app.route("/remove_product_from_cart", methods=['POST'])
def handle_remove_product_from_cart():
    return process_remove_product_from_cart(request)


@app.route("/get_cart", methods=['GET'])
def handle_get_cart():
    return process_get_cart(request)


@app.route("/list_all_achievements", methods=['GET'])
def handle_list_all_achievements():
    return process_list_all_achievements()


@app.route("/like_product", methods=['POST'])
def handle_like_product():
    return process_like_product(request)


@app.route("/unlike_product", methods=['POST'])
def handle_unlike_product():
    return process_unlike_product(request)


@app.route("/list_liked_products", methods=['GET'])
def handle_list_liked_products():
    return process_list_liked_products(request)


@app.route("/list_all_products", methods=['GET'])
def handle_list_all_products():
    return process_list_all_products()


@app.route("/buy_cart", methods=['GET'])
def handle_buy_cart():
    return process_buy_cart(request)


@app.route("/list_orders", methods=['GET'])
def handle_list_orders():
    return process_list_orders(request)


@app.route("/create_thanksgiving", methods=['POST'])
def handle_create_thanksgiving():
    return process_create_thanksgiving(request)


@app.route("/list_thanksgivings", methods=['GET'])
def handle_list_thanksgiving():
    return process_list_thanksgivings(request)
