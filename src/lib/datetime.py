from datetime import datetime


class Format:
    ISO_DATETIME = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def is_format(cls, val):
        return val in [cls.ISO_DATETIME]


def str_to_datetime(str_dt, ft=Format.ISO_DATETIME):
    try:
        return datetime.strptime(str_dt, ft)
    except (ValueError, TypeError):
        return None


def to_iso(dt):
    return dt.isoformat()
