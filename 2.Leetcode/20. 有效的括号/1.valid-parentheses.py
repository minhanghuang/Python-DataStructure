"""
https://leetcode-cn.com/problems/valid-parentheses/
"""


class Solution:
    def __init__(self):

        self.dict_val = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

    def isValid(self, s: str) -> bool:

        stack = []

        for foo in s:

            if foo in self.dict_val:

                stack.append(foo)
            else:
                try:
                    x = stack.pop()
                except:
                    return False
                if self.dict_val[x] != foo:
                    return False
        if stack:
            return False
        return True
