first_num = int(input('Introduzca un numero: '))
second_num = int(input('Introduzca un numero: '))

for num in range(1, first_num):
    if first_num % num == 0 and second_num % num == 0:
        max_divisor = num  
print(f'El maximo comun divisor es: {max_divisor}')