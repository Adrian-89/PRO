# *********
# BANAGRAMA
# *********


def run(word1: str, word2: str) -> bool:
    word1.split()
    if word1.split() in word2:
        result = True
    else:
        result = False

    is_banagram = result

    return is_banagram


if __name__ == '__main__':
    run('gabana', 'banagrama')
