# ******************
# SUMA CRIPTOGRÁFICA
# ******************
from pathlib import Path


def run(crypto_path: Path) -> float:
    with open(crypto_path) as f:
        for line in f:
            outline = line[0:3:2]
    sum_cr = outline

    return sum_cr


if __name__ == '__main__':
    run('data/sum_crypto/data1.crypto')
