class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s = ""
        for foo in digits:
            s = "".join((s, str(foo)))
        i = int(s) + 1

        ret = []
        for foo in str(i):
            ret.append(int(foo))

        return ret
