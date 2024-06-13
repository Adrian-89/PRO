# ********************************
# ENUMERANDO ELEMENTOS MODO HUMANO
# ********************************


def run(items: str) -> str:
    splitted = items.replace(':', ', ', 2)
    items.rsplit(splitted)
    # double_replace = splitted.replace
    enum_items = items.rsplit(splitted)

    return enum_items


if __name__ == '__main__':
    run('apples')
