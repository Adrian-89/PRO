# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path

STRIP_CHARS = '.,:;()'


def run(input_path: Path) -> str:
    f = open(input_path)
    max_length, longest_word = 0, ''
    for line in f:
        words = line.strip().split()
        clean_words = [w.strip(STRIP_CHARS) for w in words]
        for word in clean_words:
            if len(word) >= max_length:
                max_length = len(word)
                longest_word = word
    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')
