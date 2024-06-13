# ******************
# CONTANDO DIVISORES
# ******************


def run(number: int) -> int:
    div_count = 0
    for div_count in range(2, number):
        if number % div_count != 0:
            div_count += 1
        else:
            div_count += 0

    num_divisors = div_count

    return num_divisors


if __name__ == '__main__':
    run(67)
