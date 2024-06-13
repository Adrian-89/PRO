import sys

append_ = 0
values = [int(num) for num in sys.argv[1:]]
result = (sum(values) / len(values), 2)
print(result)
