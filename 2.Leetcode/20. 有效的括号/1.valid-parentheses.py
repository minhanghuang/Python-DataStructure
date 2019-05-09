"""
https://leetcode-cn.com/problems/valid-parentheses/
"""


list_parentheses = [")", "}", "]"]
dict_parentheses = {
    "(": ")",
    "{": "}",
    "[": "]"
}


class Solution:
    def isValid(self, s: str) -> bool:
        print(s)

        list_stack = []
        for foo in s:

            if foo not in list_parentheses:
                list_stack.append(foo)

            else:
                try:
                    temp = list_stack.pop()
                    if dict_parentheses[temp] != foo:
                        return False
                except:
                    return False
        if list_stack:
            return False

        return True
