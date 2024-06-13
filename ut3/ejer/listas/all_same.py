# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    box = []
    for result in items:
        if result == items:
            box.append(result)
        elif box == items:
            all_same = True
        else:
            all_same = False
    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])
