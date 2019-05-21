class Solution:
    def twoSum(self, nums, target):

        for num in nums:

            other = target - num

            if other in nums:
                nums_copy = nums.copy()
                nums_copy.remove(num)
                if other in nums_copy:
                    return [nums.index(num), nums_copy.index(other) + 1]

        return []




# 比较好的答案 :

# class Solution:
#     def twoSum(self, nums, target):
#         hashmap = {}
#         for i,x in enumerate(nums):
#             y = target - x
#             if y in hashmap:
#                 return hashmap[y],i
#             hashmap[x] = i