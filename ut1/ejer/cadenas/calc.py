value1 = input('ingrese numeros: ')
value2 = input('ingrese numeros: ')
value3 = int(value1, 10)
value4 = int(value2, 10)

suma = value3 + value4
resta = value3 - value4
multi = value3 * value4
div = value3 / value4

print(value3, '+', value4, '=', suma, sep='')
print(value3, '-', value4, '=', resta, sep='')
print(value3, '*', value4, '=', multi, sep='')
print(value3, '/', value4, '=', div, sep='')
