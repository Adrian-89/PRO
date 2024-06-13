# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    freq = {}
    with open(input_path) as f:
        for line in f:
            words = line.lower().strip().split()
            for word in words:
                freq[word] = freq.get(word, 0) + 1
    freq = {k: v for k, v in freq.items() if v >= lower_bound}
    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)
