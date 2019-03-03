from flask import request

from src.lib import get_keys
from src.lib.errors import Code
from src.lib.exceptions import BadRequest


def get_request_data(select_only=None):
    if request.is_json:
        request_data = request.get_json(force=True)
        if select_only:
            return get_keys(request_data, select_only)

        return request_data

    raise BadRequest(Code.BODY_NOT_JSON)


def get_request_headers():
    return request.headers
