"""
题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种方法？
"""



def fib(max_val):

    a, b, n = 0, 1, max_val

    while n:

        a, b = b, a+b
        n -= 1

    return b

n = 3

ret = n if n <= 2 else fib(n)
print(ret)