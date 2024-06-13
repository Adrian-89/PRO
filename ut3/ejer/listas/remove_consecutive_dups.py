# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    new_value_dups = []

    for values in items:
        if values[:] + 1 == items:
            new_value_dups.append(values)
    result = new_value_dups

    return result


if __name__ == '__main__':
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
