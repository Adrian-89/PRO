# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    with open(text_path) as f:
        outline = []
        for line in f:
            num_tabs = line.rstrip().count('\t')
            title = line.strip()
            outline.append((num_tabs + 1, title))

    md_path = 'data/txt2md/outline.md'
    with open(md_path, 'w') as f:
        for num_tabs, title in outline:
            hashtag = '#' * num_tabs
            f.write(f'{hashtag} {title}\n')

    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')
