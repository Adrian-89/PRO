# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    position = values[0]
    for max_num in values:
        if max_num > position:
            position = max_num

    max_value = position

    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])
