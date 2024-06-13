# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = {}
    for items in sentence:
        if items not in counter:
            counter[items] = 1
        else:
            counter[items] += 1

    return counter


if __name__ == '__main__':
    run('boom')
