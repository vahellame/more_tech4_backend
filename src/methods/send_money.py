from flask import Request


def process_send_money(request: Request):
    token = request.headers['Token']
    return ''
