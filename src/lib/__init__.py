# `False` and 0 - does not mean that val is empty.
SPECIAL_BOOL = [0, False]


def is_empty(val):
    # Do not check for empty values.
    return val not in SPECIAL_BOOL and not bool(val)


def to_str(value):
    if value is None:
        return ""

    return str(value)


def to_int(value, default=None):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def to_bool(value):
    if value == "False" or value == "false" or value == "0":
        return False

    return bool(value)


def merge_dicts(*dicts):
    result = dict()
    for d in dicts:
        result.update(d)

    return result


def del_keys(d, keys):
    return {k: v for k, v in d.items() if k not in set(keys)}


def get_keys(d, keys):
    return {k: d[k] for k in set(keys) if k in d}


def is_sequence(o):
    return type(o) in {list, tuple, set, frozenset, bytearray}
