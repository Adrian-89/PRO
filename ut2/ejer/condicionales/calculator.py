value1 = input('Ingrese numeros')
value2 = input('Ingrese numeros')
value3 = input('Seleccione operador: +-*/')
value4 = int(value1, 10)
value5 = int(value2, 10)

suma = value4 + value5
resta = value4 - value5
multi = value4 * value5
div = value4 / value5

match value3:
    case '+':
        print(value4, '+', value5, '=', suma, sep='')
    case '-':
        print(value4, '-', value5, '=', resta, sep='')
    case '*':
        print(value4, '*', value5, '=', multi, sep='')
    case '/':
        print(value4, '/', value5, '=', div, sep='')
