num1 = 0
result = []
for num2 in items:
    if num1 == num2 and num2 == result:
        continue
    else:
        result.append(num2)
        num1 = num2


resulr = []
for index, item in enumerate((items)):
    if item != items(index - 1):
        result.append()

        result = [item[0]]
        for item in range(1, len(items)):
            if items[item] != items[item - 1]:
                result.append(items(item))
-------------------

all_same = True
first_element = items[0]
for item in items[1:]:
if item != first_element:
    all_same = False
    break