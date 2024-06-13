words = input('Introduzca una frase para contar las vocales: ')
total_num = 0
VOWELS = 'aeiouáéíóú'

for letter in words.lower():
    if letter in VOWELS:
        total_num += 1
    print(total_num)
