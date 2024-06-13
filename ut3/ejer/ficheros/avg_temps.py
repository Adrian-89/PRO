# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    a = open(input_path)
    a2 = open(output_path, 'w')
    with open(output_path) as b:
        for item in b:
           teperatures= item.strip().split()

        
    for code in output_path:
        all_inputs = a.writelines(code + '\n')
    

    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')
