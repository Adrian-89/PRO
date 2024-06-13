def add(numbers, b):
    if isinstance(numbers) == list:
      result = 0
      for number in numbers:
           result += number
        return result
    if b != None:

#my_numbers = [8, 9, 32, 5, 15, 20]
if sum(numbers) == add(numbers):
    print('Good!!!')
else:
    print('Bad!!!')
print(add(my_numbers))
