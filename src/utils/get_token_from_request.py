from flask import abort, Request


def get_token_from_request(request: Request):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
        return token
    abort(404)
