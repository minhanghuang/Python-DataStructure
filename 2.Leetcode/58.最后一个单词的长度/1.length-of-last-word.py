class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        list_s = s.split(" ")
        for i in range(-1, -len(list_s) - 1, -1):

            if list_s[i]:
                return len(list_s[i])

        return 0
