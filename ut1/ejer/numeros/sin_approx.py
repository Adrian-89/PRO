# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
    coefi3 = 180 - x
    coefi1 = 4 * x * coefi3
    coefi2 = 40500 - x * coefi3
    sin = coefi1 / coefi2

    return sin


if __name__ == '__main__':
    run(90)
