class BadRequest(Exception):
    def __init__(self, code=400, errors=None):
        super(BadRequest, self).__init__()

        message = {
            'status': 400,
            'code': code,
        }

        if errors is not None:
            message.update({'errors': errors})

        self.message = message


class NotFound(Exception):
    def __init__(self, code=404, errors=None):
        super(NotFound, self).__init__()

        message = {
            'status': 404,
            'code': code,
        }

        if errors is not None:
            message.update({'errors': errors})

        self.message = message


def is_exception(instance):
    return isinstance(instance, Exception)
