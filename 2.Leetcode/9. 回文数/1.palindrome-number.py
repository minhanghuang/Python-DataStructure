"""
https://leetcode-cn.com/problems/palindrome-number/
"""




class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        str_ret = ""

        for foo in list(str(x)):
            str_ret = foo + str_ret

        if int(str_ret) == x:
            return True
        return False

