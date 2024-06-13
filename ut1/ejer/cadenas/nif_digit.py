# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
    nif_letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
    nif_value = int(nif)
    division = nif_value % 23
    letter_nif = nif_letters[division]
    wnif = f'{nif}{letter_nif}'

    return wnif


if __name__ == '__main__':
    run('78654355')
