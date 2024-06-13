# *************************
# SIMULANDO EL COMANDO TAIL
# *************************
from pathlib import Path


def run(file: Path, n: int) -> str:
    data = [] 
    with open(file) as f:
        for line in f:

            if n:
                data.append() = line[-30].strip()

    return lines


if __name__ == '__main__':
    run('data/tail/nba_season22.txt', 3)
