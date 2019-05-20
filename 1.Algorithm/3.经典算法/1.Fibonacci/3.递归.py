

def fib(n):

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

for foo in  range(10):

    print(fib(foo))

