enter_number = int(input('Introduzca un número: '))
count = 0
for value in range(enter_number):
    if value % 3 == 0:
        count += value
        print(value)
        if count >= enter_number:
            break
