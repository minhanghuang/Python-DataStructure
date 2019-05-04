# 冒泡排序
# 有小到大(左->右)
#



class Solution(object):

    def bubble(self):

        nums = list(eval(input("请输入需要排序的数据,逗号隔开,回车结束:")))

        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(len_nums-i-1):
                if nums[len_nums-j-1] < nums[len_nums-j-1-1]: # 右<左 -> 浮
                    nums[len_nums - j - 1], nums[len_nums-j-1-1] = \
                    nums[len_nums-j-1-1] ,nums[len_nums-j-1]
        return nums

print(Solution().bubble())



