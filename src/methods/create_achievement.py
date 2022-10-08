# -*- coding: utf-8 -*-

from flask import Request


def process_create_achievement(request: Request):
    data = request.get_json()
    title = data['title']
    description = data['title']
    price = data['price']
    photo_id = data['photo_id']
    achievnet = {
        'tx': 0xf21e4d805e05f7d3fc8bdb32505d505c6aa840f1825e2bdcc3a2522cb641eeb4,
        'uri':
    }

