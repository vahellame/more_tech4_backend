# -*- coding: utf-8 -*-

from flask import Request


def process_create_achievement(request: Request):
    data = request.get_json()
    title = data['title']
    description = data['title']
    price = data['price']
    photo_id = data['photo_id']

