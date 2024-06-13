import re


def is_valid_float(number: str) -> bool:
    # regex = r'^\d?^\.?\de\d-?'
    regex = r'(-*\d.)*(\de\d\.?)(-\d)*'
    return re.fullmatch(regex, number) is not None
