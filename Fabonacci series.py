
def fibanoci(num):
    a = 0
    b = 1

    if num<1:
        return -1
    if num == 1:
        return a
    if num == 2:
        return b

    counter=3  
    while counter <= n:
        fib_n = a + b
        a = b
        b = fib_n
        counter += 1  
    return fib_n


n=10
print(fibanoci(9))