# ****************
# PRODUCTO ESCALAR
# ****************


def run(vector1: list, vector2: list) -> float:
    process = 0
    if len(vector1) == len(vector2):
        for v1, v2 in zip(vector1, vector2):
            process += v1 * v2
    else:
        process = None

    dprod = process
    return dprod


if __name__ == '__main__':
    run([4, 3, 8, 1], [9, 2, 7, 3])
