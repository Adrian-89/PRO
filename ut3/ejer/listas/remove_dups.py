# *********************
# ELIMINANDO DUPLICADOS
# *********************


def run(nums_dups: list) -> list:
    new_nums_dups = []

    for nums in nums_dups:
        if nums not in new_nums_dups:
            new_nums_dups.append(nums)

    nums_unique = new_nums_dups

    return nums_unique


if __name__ == '__main__':
    run([2, 3, 2, 2, 1, 5, 4, 2, 4, 9])
