enter_number = int(input('Introduzca un número: '))
pow_accumulation = 1

for num in range(1, enter_number + 1):
    pow_result = num**2
    pow_accumulation *= pow_result
    print(pow_accumulation)
    
