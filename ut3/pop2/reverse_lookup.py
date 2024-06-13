# ********************
# CLAVES DESDE VALORES
# ********************


def run(items: dict, target_value: int) -> tuple:
    Result = {}
    for key, value in items.items():
        if value == target_value:
            Result[key] = value

        source_keys = tuple(Result)

    return source_keys


if __name__ == '__main__':
    run({'A': 1, 'B': 2, 'C': 3, 'D': 3, 'E': 4}, 3)
