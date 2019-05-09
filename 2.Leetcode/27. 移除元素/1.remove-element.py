"""
https://leetcode-cn.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums_copy = nums.copy()

        for foo in nums:

            if val == foo:
                nums_copy.remove(val)

        # print(nums_copy)
        nums[:len(nums_copy)] = nums_copy
        # print(nums)



        return len(nums_copy)
