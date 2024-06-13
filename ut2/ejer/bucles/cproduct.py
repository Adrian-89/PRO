first_word = input('Introduzca las cordenadas de los puntos: ')
second_word = input('Introduzca el segundo punto cartesiano: ')

for letter in first_word:
    for number in second_word:
        print(f'{letter}{number}')
