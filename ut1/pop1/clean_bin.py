# ****************
# EN BINARIO CLARO
# ****************


def run(number: int) -> str:
    convert_bin = bin(number)
    nbin = convert_bin[2:]
    return nbin


if __name__ == '__main__':
    run(233)
