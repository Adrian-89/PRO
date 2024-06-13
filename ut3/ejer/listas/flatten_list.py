# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    flattened_list = []
    str(elements)
    for data in elements:
        if isinstance(data, list):
            if data in elements:
                elements.pop(data) + elements
                flattened_list.append(elements)

            flatten_elements = list(flattened_list)

    return flatten_elements


if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])
