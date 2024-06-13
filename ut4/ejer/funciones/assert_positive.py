# *******************************
# ASEGURANDO ARGUMENTOS POSITIVOS
# *******************************


def assert_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                return 0
        for kwarg in kwargs.values():
            if kwarg <= 0:
                return 0

        return func(*args, **kwargs)

    return wrapper


@assert_positive
def factorial(number: int):
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result
