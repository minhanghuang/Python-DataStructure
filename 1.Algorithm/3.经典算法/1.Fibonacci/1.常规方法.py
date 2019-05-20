

def fib(max_val):

    a, b, n = 0, 1, max_val

    while n:

        print(a)
        a, b = b, a+b
        n -= 1

    return None

fib(10)
