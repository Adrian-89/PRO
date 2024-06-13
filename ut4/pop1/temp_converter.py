# ************************
# CONVERSOR DE TEMPERATURA
# ************************


def temp_converter(num: float):
    def run(source: str, temp: float) -> float:

        f2c = (temp - 32) / 1.8
        c2f = (temp * 1.8) + 32
        if source == 'c2f':
            op = c2f
        elif source == 'f2c':
            op = f2c
        else:
            None
        return op

    return run
