"""
https://leetcode-cn.com/problems/roman-to-integer/
"""
dict_roma = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

dict_s = {
    "I": ["V", "X"],
    "X": ["L", "C"],
    "C": ["D", "M"],
}


class Solution:
    def romanToInt(self, s: str) -> int:

        ret = 0

        for i, val in enumerate(list(s)):

            if val in ["I", "X", "C"]:
                try:
                    if list(s)[i + 1] in dict_s[val]:
                        ret += (dict_roma[list(s)[i + 1]] - dict_roma[val])
                        ret -= dict_roma[list(s)[i + 1]]
                    else:
                        ret += dict_roma[val]
                except:
                    ret += dict_roma[val]
            else:
                ret += dict_roma[val]

        return ret


