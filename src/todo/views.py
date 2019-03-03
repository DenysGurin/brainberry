from flask.views import MethodView

from src.todo.lib import bl
from src.todo import serializers

from src.lib.request import get_request_data
from src.lib.errors import Code
from src.lib.exceptions import BadRequest, NotFound


class ListAPI(MethodView):

    def get(self, list_id=None):
        """
        Show list of Lists if 'list_id' is None, otherwise show List with _id == list_id
        :param list_id: bsonType: objectId
        """
        if list_id is None:
            return serializers.lists(bl.fetch_lists())

        _list = bl.fetch_list(list_id)
        if not _list:
            raise NotFound(Code.LIST_NOT_EXIST)

        return serializers.one_list(_list)

    def post(self):
        """
        Create new List
        """
        return serializers.one_list(
            bl.create_list(**get_request_data())
        )

    def put(self, list_id):
        """
        Update existed List
        """
        if not bl.fetch_list(list_id):
            raise NotFound(Code.LIST_NOT_EXIST)

        return serializers.one_list(
            bl.update_list(list_id, **get_request_data())
        )

    def delete(self, list_id):
        """
        Delete existed List
        """
        if not bl.fetch_list(list_id):
            raise NotFound(Code.LIST_NOT_EXIST)

        return serializers.one_list(
            bl.delete_list(list_id)
        )


class ItemAPI(MethodView):

    def post(self):
        """
        Create new Item
        """
        data = get_request_data()
        if not bl.fetch_list(data.get('list_id')):
            raise BadRequest(Code.LIST_NOT_EXIST)

        return serializers.one_item(
            bl.create_item(**data)
        )

    def put(self, item_id):
        """
        Update existed Item
        """
        if not bl.fetch_item(item_id):
            raise NotFound(Code.ITEM_NOT_EXIST)

        data = get_request_data()
        if data.get('list_id'):
            if not bl.fetch_list(data['list_id']):
                raise NotFound(Code.LIST_NOT_EXIST)

        return serializers.one_item(
            bl.update_item(item_id, **data)
        )

    def delete(self, item_id):
        """
        Delete existed Item
        """
        if not bl.fetch_item(item_id):
            raise NotFound(Code.ITEM_NOT_EXIST)

        return serializers.one_item(
            bl.delete_item(item_id)
        )
