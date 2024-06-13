first_num = 0
second_num = 1

for _ in range(100):
    fibo_chain = first_num + second_num
    first_num = second_num
    second_num = fibo_chain

    print(fibo_chain)
