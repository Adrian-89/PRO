LIMIT_DOMINIO = 6

for first_num in range (LIMIT_DOMINIO + 1):
    for second_num in range(first_num, LIMIT_DOMINIO + 1):
        print((f'{first_num}|{second_num}'), end=' ')
    print()