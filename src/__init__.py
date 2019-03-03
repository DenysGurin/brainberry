from werkzeug.exceptions import (
    Unauthorized, NotFound, Forbidden, MethodNotAllowed,
)

from flask import Flask, jsonify
from flask.logging import create_logger

from pymongo import MongoClient

from config import Config

from src.lib import exceptions
from src.lib.json import ApiJSONEncoder
from src.lib.response import ApiResponse
from src.lib.mongo import create_collections


app = Flask("app")
client = MongoClient(Config.DB_HOST, Config.DB_PORT)
db = client[Config.DB_NAME]

from src.todo.views import ListAPI, ItemAPI
from src.todo.collections import List, Item

create_collections(db, List)
create_collections(db, Item)

create_logger(app)

app.config.from_object(Config)
app.json_encoder = ApiJSONEncoder
app.response_class = ApiResponse

list_view = ListAPI.as_view('lists_api')
app.add_url_rule('/api/lists', view_func=list_view, methods=['GET', 'POST'])
app.add_url_rule('/api/lists/<string:list_id>', view_func=list_view, methods=['GET', 'PUT', 'DELETE'])

item_view = ItemAPI.as_view('item_api')
app.add_url_rule('/api/items', view_func=item_view, methods=['POST'])
app.add_url_rule('/api/items/<string:item_id>', view_func=item_view, methods=['PUT', 'DELETE'])


@app.errorhandler(exceptions.BadRequest)
def bad_request(error):
    return jsonify(error)


@app.errorhandler(exceptions.NotFound)
def not_found(error):
    return jsonify(error)


@app.errorhandler(Unauthorized)
def unauthorized(_):
    return jsonify({
            'status': 401,
            'code': 401,
        })


@app.errorhandler(Forbidden)
def forbidden(_):
    return jsonify({
        'status': 403,
        'code': 403,
    })


@app.errorhandler(NotFound)
def not_found(_):
    return jsonify({
        'status': 404,
        'code': 404,
    })


@app.errorhandler(MethodNotAllowed)
def not_allowed(_):
    return jsonify({
        'status': 405,
        'code': 405,
    })
