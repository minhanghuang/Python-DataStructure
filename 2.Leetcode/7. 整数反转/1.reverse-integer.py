"""
https://leetcode-cn.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:

        first = ""

        if x < 0:
            first = "-"

        x = abs(x)

        str_ret = ""
        for foo in list(str(x)):
            str_ret = foo + str_ret

        str_ret = first + str_ret

        ret = int(str_ret)
        import math

        if ret > -math.pow(2, 31) and ret < math.pow(2, 31):

            return ret
        else:
            return 0



