"""
https://leetcode-cn.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        try:
            min_i = len(strs[0])
        except:
            return ""
        list_tar = []

        tar = strs[0]
        len_tar = len(tar)

        if not tar:
            return ""

        for foo in range(0, len_tar):

            f = tar[0:foo + 1]

            for s in strs:
                if f not in s[0:foo + 1]:
                    return f[:-1]

        if f == tar:
            return f

        return ""
