ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

enter_word = input('Introduzca una frase: ').lower()
find_result = None

for letter in enter_word:
    if letter in ALPHABET:
        find_result = True
    else:
        find_result = False
        break

if find_result:
    print('No se han encontrado caracteres no alfabéticos')
else:
    print('Se han encontrado caracteres no alfabéticos')