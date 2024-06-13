# *************************
# PRIMER ELEMENTO DUPLICADO
# *************************


def run(numbers: list) -> int:
    target = {}
    fdup = -1
    for item in numbers:
        if item in target:
            fdup = item
            break
        else:
            target[item] = 1

    return fdup


if __name__ == '__main__':
    run([2, 3, 5, 3, 2])
