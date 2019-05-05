"""
# 选择排序

选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，
存放在序列的起始位置，直到全部待排序的数据元素排完

"""


class Solution(object):

    def selection(self):

        nums = list(eval(input("请输入需要排序的数据,逗号隔开,回车结束:")))

        len_bums = len(nums)
        for i in range(len_bums):
            min_value = [i,nums[i]]
            for j in range(i+1,len_bums):
                if min_value[1] > nums[j]:
                    min_value[1], nums[j] = nums[j], min_value[1]
                    min_value[0] = j

            nums[i] = min_value[1]

        return nums

print(Solution().selection())




