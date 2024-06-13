# ********************
# EN LAS BASES DEL ADN
# ********************


def run(dna: str) -> tuple:
    MAX_LETTERS = len(dna)
    nº_A = dna.count('A')
    nº_G = dna.count('G')
    nº_T = dna.count('T')
    nº_C = dna.count('C')
    adenines_rate = nº_A / MAX_LETTERS * 100
    guanines_rate = nº_G / MAX_LETTERS * 100
    thymines_rate = nº_T / MAX_LETTERS * 100
    cytosines_rate = nº_C / MAX_LETTERS * 100

    return adenines_rate, guanines_rate, thymines_rate, cytosines_rate


if __name__ == '__main__':
    run('GGTTACCAACCCAGTCGAAAATTTGGTCAGGG')
