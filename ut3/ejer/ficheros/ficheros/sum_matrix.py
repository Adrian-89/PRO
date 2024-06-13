# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    matrix1 = []
    with open(matrix1_path) as f:
        for line in f:
            matrix1.append([int(v) for v in line.strip().split()])

    matrix2 = []
    with open(matrix2_path) as f:
        for line in f:
            matrix2.append([int(v) for v in line.strip().split()])

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1)):
            r = matrix1[i][j] + matrix2[i][j]
            row.append(r)
        result.append(row)

    result_path = 'data/sum_matrix/result.dat'
    with open(result_path, 'w') as f:
        for row in result:
            buffer = ' '.join(str(v) for v in row)
            f.write(f'{buffer}\n')

    return filecmp.cmp(result_path, 'data/sum_matrix/.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')
