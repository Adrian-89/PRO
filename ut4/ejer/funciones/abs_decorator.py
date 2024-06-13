# *******************************
# DECORANDO CON VALORES ABSOLUTOS
# *******************************
def fabs(func):
    def wrapper(*args, **kwargs):
        result = abs(func(*args, **kwargs))
        return result

    # return func(abs(a), abs(b)) forma correcta de hacerlo
    return wrapper


@fabs
def fprod(a: int, b: int) -> int:
    return a * b


# decorated_fprod = fabs(fprod)
