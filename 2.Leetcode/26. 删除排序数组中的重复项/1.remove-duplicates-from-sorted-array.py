class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for i, num in enumerate(nums):

            try:

                while num == nums[i + 1]:
                    nums.pop(i + 1)
            except:
                break

        return len(nums)
