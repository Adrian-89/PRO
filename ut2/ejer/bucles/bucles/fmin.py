minimum_result = None

for num in range(-9,9):
    math_formu = num **2 - 6 * num + 3
    if minimum_result is None or math_formu < minimum_result:
        minimum_result = math_formu
        x = num

print(f'x = {x}: f(x) = {minimum_result}')
        