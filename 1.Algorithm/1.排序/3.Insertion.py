"""
# 插入排序

要求在这个已经排好的数据序列中插入一个数，但要求插入后此数据序列仍然有序，
这个时候就要用到一种新的排序方法——插入排序法,插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。
"""


class Solution(object):

    def insertion(self):

        nums = list(eval(input("请输入需要排序的数据,逗号隔开,回车结束:")))

        len_nums = len(nums)
        for i in range(len_nums):

            for j in range(i):

                if nums[i-j] < nums[i-1-j]:
                    nums[i-j], nums[i-1-j] = \
                    nums[i-1-j], nums[i-j]
                else:
                    break

        return nums

print(Solution().insertion())




