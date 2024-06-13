LETTER_U = 'U'
LETTER_D = 'D'
LETTER_X = 'X'
enter_limit = int(input('Introduzca el límite para su  mosaico: '))

for row in range(enter_limit):
    for colum in range(enter_limit):
        if row < colum:
            print(LETTER_U, end=' ')
        elif colum < row:
            print(LETTER_D, end=' ')
        else:
            print(LETTER_X, end=' ')
    print()
