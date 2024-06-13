# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    buscar_void = fullname.find(' ')
    first_zone = fullname[:buscar_void]
    second_zone = fullname[buscar_void + 1 :]

    swapname = f'{second_zone} {first_zone}'

    return swapname


if __name__ == '__main__':
    run('John McClane')
