for first in range(33,128):
    if first < 100:
        code = f'0{first}'
    else:
        code = f'{first}' 
    print(f'{code} {chr(first)}')   
print()    