# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/common_words/output.txt'
    f = open(input_path)
    lines = [line.strip().lower().split() for line in f]
    f2 = open(output_path, 'w')
    for line1 in lines:
        for line2 in lines:
            common_words = set(line1) & set(line2)
            f2.write(f'{len(common_words)}\n')
    f2.close()
    return filecmp.cmp(output_path, 'data/common_words/.expected', shallow=False)


if __name__ == '__main__':
    run('data/common_consonants/minizen.txt')
