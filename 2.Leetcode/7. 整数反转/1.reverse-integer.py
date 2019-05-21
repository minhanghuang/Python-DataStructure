"""
https://leetcode-cn.com/problems/reverse-integer/
"""

import math


class Solution:
    def reverse(self, x: int) -> int:
        neg = "-" if x < 0 else ""
        x = int("".join((neg, str(abs(x))[::-1])))

        if x > math.pow(2, 31) - 1 or x < math.pow(-2, 31):
            return 0

        return x




