enter_num = int(input('Introduzca el eje x: '))
second_num = int(input('Introduzca el eje y: '))
x_pos = 0
y_pos = 0
print(x_pos, y_pos)
first_move = True
second_move = False

while x_pos < enter_num and y_pos < second_num:
    if first_move:
        x_pos += 1
        y_pos += 2
        second_move = True
        first_move = False
    elif second_move:
        x_pos += 2
        y_pos += 1
        first_move = True
        second_move = False
    print(x_pos,y_pos)

    
    