# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    outline = []
    with open(data_path) as f:
        for line in f:
            outline.append([int(v) for v in line.strip().split()])
    result = []
    for item in range(len(outline)):
        colum = []
        for item2 in range(len(outline)):
            r = outline[item][item2] + outline[item][item2]
            colum.append(r)
        result.append(colum)
    csum = tuple(result)

    return csum


if __name__ == '__main__':
    run('data/sum_cols/data1.txt')
