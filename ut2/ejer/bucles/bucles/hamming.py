first_word = input('Introduzca una cadena de texto: ')
second_word = input('Introduzca una cadena de texto: ')
count = 0

for letter in range(len(first_word)):
    if first_word [letter]!= second_word[letter]:
        count+= 1    
print(count)