# ****************
# CONTANDO VOCALES
# ****************


def run(text: str) -> int:
    total_num = 0
    VOWELS = 'aeiouáéíóú'

    for letter in text.lower():
        if letter in VOWELS:
            total_num += 1
    num_vowels = total_num

    return num_vowels


if __name__ == '__main__':
    run('El camión chocó contra el árbol')
