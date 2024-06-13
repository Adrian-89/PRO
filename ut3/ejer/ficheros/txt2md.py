# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'
    with open(text_path) as f:
        with open("data/txt2md/outline.txt", 'w')
    
    for line in f:
        line = line.strip().split()
    for item in line:
        item.replace('\n', '#')
        f.close()
    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')
