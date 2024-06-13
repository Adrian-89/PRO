# ********************************
# PRIMER ELEMENTO REPETIDO N-VECES
# ********************************


def run(numbers: list, nrep: int) -> int:
    target = {}
    target_num = -1
    for item in numbers:
        if item in target:

            nrep -= 1
            target_num = item
            break
        else:
            target[item] = 1

    return target_num


if __name__ == '__main__':
    run([2, 3, 5, 3, 2, 1, 8, 2], 3)
