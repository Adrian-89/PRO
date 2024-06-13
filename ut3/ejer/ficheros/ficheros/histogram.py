# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    with open(data_path) as f:
        data = f.read().strip()

    counter = {}
    for d in data:
        counter[d] = counter.get(d, 0) + 1

    histogram_path = 'data/histogram/histogram.txt'
    with open(histogram_path, 'w') as f:
        for label in sorted(counter):
            count = counter[label]
            bar = '█' * count
            f.write(f'{label} {bar} {count}\n')

    return filecmp.cmp(histogram_path, 'data/histogram/.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')
