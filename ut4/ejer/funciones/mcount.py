# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: tuple, target: int):
    counter = 0
    for item in items:
        if item == target:
            counter += 1
    return counter
