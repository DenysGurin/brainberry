from werkzeug.wrappers import Response

from flask.json import jsonify

from src.lib.cors import wrap_cors


class ApiResponse(Response):

    @classmethod
    @wrap_cors(origin="*")
    def force_type(cls, obj, environ=None):
        if isinstance(obj, dict):
            obj = jsonify(obj)
        return super(ApiResponse, cls).force_type(obj, environ)
