def is_even(a):
    if a % 2 == 0:
        return True
    return False


def split_evenly(b):
    evens = []
    odds = []
    for number in b:
        if is_even(number):
            evens.append(number)
        odds.append(number)
    return evens, odds


if is_even(3):
    print("es par")
else:
    print("es impar")
