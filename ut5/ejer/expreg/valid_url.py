import re


def is_valid_url(url: str) -> bool:
    regex = r'^https?:\//.+\.+.+\w'
    return re.fullmatch(regex, url) is not None
