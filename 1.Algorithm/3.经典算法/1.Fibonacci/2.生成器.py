

def fib(max_val):

    a, b, n = 0, 1, max_val

    while n:

        yield a
        a, b = b, a+b
        n -= 1

    return None

for foo in fib(10):

    print(foo)
