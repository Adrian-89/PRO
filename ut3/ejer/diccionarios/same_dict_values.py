# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    all_same = True
    values = items.values()
    f_value = values[0]
    for value in values:
        if value != f_value:
            all_same = False
            break

    return all_same


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})
