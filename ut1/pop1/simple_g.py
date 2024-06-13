# ********************
# UNA SENCILLA FUNCIÓN
# ********************


def run(a: int, b: int) -> float:
    first_op = -a * ((abs(b)) ** 0.5)
    second_op = b * a**2 * ((abs(a)) ** 0.5)
    result_op = first_op / second_op
    redondeo = round(result_op, 7)
    G = redondeo

    return G


if __name__ == '__main__':
    run(-5, 7)
