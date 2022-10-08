from flask import Request


def process_create_achievement(request: Request):
    data = request.get_json()
    title = data['title']
    description = data['title']
    price = data['price']
