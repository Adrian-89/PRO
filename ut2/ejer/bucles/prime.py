insert_num = int(input('Inserte un numero para saber si es primo: '))
for prime_result in range(2, insert_num // 2):
    if insert_num % prime_result == 0:
        print('No es primo')
        break

    else:
        print('Es primo')
