# ***********
# MITAD FUERA
# ***********


def run(values: set) -> set:
    half_out_values = set()
    for itrems in values:
        half_item = itrems // 2
        if half_item not in values:
            half_out_values.add(half_item)

    return half_out_values


if __name__ == '__main__':
    run({50, 100, 4, 6, 12})
