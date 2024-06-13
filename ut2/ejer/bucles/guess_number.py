WINNER = 87
attempts = 0

while True:
    enter_number = int(input('Introduzca un numero: '))
    if enter_number == WINNER:
        attempts += 1
        break
    elif enter_number < WINNER:
        final_word = 'Menor'
        attempts += 1
    else:
        final_word = 'Mayor'
        attempts += 1
    print(final_word)
print(f'Felicidades, has encontrado el numero en {attempts} intentos')
