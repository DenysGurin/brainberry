from __future__ import absolute_import

import json

from bson import ObjectId
from bson.dbref import DBRef

from flask.json import JSONEncoder

from src.lib.exceptions import is_exception


class ApiJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, map):
            return list(obj)

        elif isinstance(obj, set):
            return list(obj)

        elif isinstance(obj, tuple):
            return list(obj)

        elif isinstance(obj, ObjectId):
            return str(obj)

        elif isinstance(obj, DBRef):
            return obj.as_doc()

        elif obj is None:
            return {}

        elif is_exception(obj):
            return getattr(obj, 'message', {})

        return JSONEncoder.default(self, obj)


def loads(serialized, on_exception=None):
    try:
        return json.loads(serialized)
    except (json.JSONDecodeError, TypeError):
        return on_exception


def dumps(python):
    return json.dumps(python)
