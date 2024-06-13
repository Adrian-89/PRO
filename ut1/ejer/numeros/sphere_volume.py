# *********************
# VOLUMEN DE UNA ESFERA
# *********************


def run(radius: float) -> float:
    fracci = 4 / 3
    PI = 3.14
    r = radius**3
    volume = fracci * PI * r

    return volume


if __name__ == '__main__':
    run(5)
