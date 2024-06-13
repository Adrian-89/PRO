# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:
    set_empty1 = set()
    set_empty2 = set()
    for set_empty10, set_empty20 in input:
        set_empty1.add(set_empty10)
        set_empty2.add(set_empty20)

    output = (set_empty1, set_empty2)
    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))
