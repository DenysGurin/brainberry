def lists(i):
    if i is None:
        return {
            "lists": [],
        }

    return {
        "lists": list(i),
    }


def one_list(i):
    if i is None:
        return {}

    return i


def items(i):
    if i is None:
        return {
            "items": [],
        }

    return {
        "items": list(i),
    }


def one_item(i):
    if i is None:
        return {}

    return i
