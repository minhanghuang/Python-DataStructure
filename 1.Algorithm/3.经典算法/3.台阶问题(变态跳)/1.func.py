"""
题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
"""


def jump(n):

    while n<=2:
        return n

    return 2**(n-1)
    # return jump(n-1)*2

print(jump(5))