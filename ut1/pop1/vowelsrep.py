# *********************************
# ENCONTRANDO REPETICIÓN DE VOCALES
# *********************************


def run(text: str) -> int:
    text.lower()
    text.count()
    text.find()
    nrep = text.find(vocals)

    return nrep


if __name__ == '__main__':
    run('aaaantequera')
