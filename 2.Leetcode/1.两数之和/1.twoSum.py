class Solution:
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param nums: int
        :return: List[int]
        """

        for num in nums:

            other = target - num

            if other in nums:

                if nums.index(other) != nums.index(num):

                    return sorted([nums.index(other), nums.index(num)])

                else:
                    if nums.count(num) == 2:
                        num_index = nums.index(num)
                        nums[num_index] = 'x'
                        return sorted([num_index, nums.index(num)])




# 比较好的答案 :

# class Solution:
#     def twoSum(self, nums, target):
#         hashmap = {}
#         for i,x in enumerate(nums):
#             y = target - x
#             if y in hashmap:
#                 return hashmap[y],i
#             hashmap[x] = i