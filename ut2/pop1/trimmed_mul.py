# ******************
# PRODUCTO RECORTADO
# ******************


def run(value1: float, value2: float, vmin: float, vmax: float) -> float:
    if value1 * value2 < vmin:
        product = vmin
    elif value1 * value2 > vmax:
        product = vmax
    elif value1 * value2 > vmin < vmax:
        product = value1 * value2
    rmul = round(product, 2)

    return rmul


if __name__ == '__main__':
    run(3.21, 7.44, 0, 20.51)
