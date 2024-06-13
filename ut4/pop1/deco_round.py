# ****************************
# REDONDEANDO CON UN DECORADOR
# ****************************


def cround(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return round(result, 2)

    return wrapper


@cround
def avg(values: list) -> float:
    all_sum = sum(values)
    avg = all_sum / len(values)
    result = avg

    return result


if __name__ == '__main__':
    avg([6, 3, 9, 3, 5, 4, 5, 7, 2, 3, 6])
