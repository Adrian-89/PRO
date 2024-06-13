# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(number):
    result = 1
    if number < 0:
        return None
    for num in range(1, number + 1):
        result *= num
    return result
