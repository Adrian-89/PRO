while True:
    enter_word = input('¿Su nombre?')
    is_title = enter_word.istitle()
    if is_title:
        print('Has escrito bien tu nombre')
        break
    else:
        print('Error. Debe escribirlo otra vez')
        