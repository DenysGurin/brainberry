from bson.objectid import ObjectId

from src import db
from src.todo.collections import List, Item

from src.lib import get_keys
from src.lib.datetime import str_to_datetime
from src.lib.errors import Code
from src.lib.exceptions import BadRequest

_lists = db.get_collection(List.NAME)
_items = db.get_collection(Item.NAME)


def _validate_id(oid):
    if not ObjectId.is_valid(oid):
        raise BadRequest(Code.OBJECT_ID_INVALID)

    return oid


def _prepare_list(kwargs):
    cleaned = get_keys(kwargs, List.COLUMNS.keys())
    return cleaned


def _prepare_item(kwargs):
    cleaned = get_keys(kwargs, Item.COLUMNS.keys())
    if cleaned.get('list_id'):
        cleaned['list_id'] = ObjectId(_validate_id(cleaned.pop('list_id')))

    if cleaned.get('date'):
        cleaned['date'] = str_to_datetime(cleaned.pop('date'))

    return cleaned


def fetch_lists():
    pipeline = [
        {
            '$lookup': {
                'from': 'items',
                'localField': '_id',
                'foreignField': 'list_id',
                'as': 'items'
            }
        }
    ]
    try:
        return _lists.aggregate(pipeline)

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def fetch_list(list_id):
    pipeline = [
        {
            "$match": {
                "_id": ObjectId(_validate_id(list_id))
            },
        },
        {
            "$limit": 1
        },
        {
            '$lookup': {
                'from': 'items',
                'localField': '_id',
                'foreignField': 'list_id',
                'as': 'item'
            },
        },
    ]
    try:
        query = list(_lists.aggregate(pipeline))
        if len(query):
            return query[0]
        return

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def create_list(**kwargs):
    data = _prepare_list(kwargs)
    try:
        return fetch_list(_lists.insert_one(data).inserted_id)

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def update_list(list_id, **kwargs):
    data = _prepare_list(kwargs)
    try:
        _lists.update_one({'_id': ObjectId(_validate_id(list_id))}, {"$set": data}, upsert=False)
        return fetch_list(ObjectId(list_id))

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def delete_list(list_id):
    try:
        _lists.delete_one({'_id': ObjectId(_validate_id(list_id))})
        return fetch_list(ObjectId(list_id))

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def fetch_item(item_id):
    try:
        return _items.find_one({'_id': ObjectId(_validate_id(item_id))})

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def create_item(**kwargs):
    data = _prepare_item(kwargs)
    try:
        return fetch_item(
            _items.insert_one(data).inserted_id
        )

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def update_item(item_id, **kwargs):
    data = _prepare_item(kwargs)
    try:
        _items.update_one({'_id': ObjectId(_validate_id(item_id))}, {"$set": data}, upsert=False)
        return fetch_item(ObjectId(item_id))

    except Exception:
        raise BadRequest(Code.BODY_INVALID)


def delete_item(item_id):
    try:
        _items.delete_one({'_id': ObjectId(_validate_id(item_id))})
        return fetch_item(ObjectId(item_id))

    except Exception:
        raise BadRequest(Code.BODY_INVALID)
