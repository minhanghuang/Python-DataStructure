

# 有序列表 
# 时间复杂度O(n)
# 空间复杂度O(1)

def func(tar):

    for i,num in enumerate(tar):

        try:
            while num == tar[i+1]:
                tar.pop(i+1)
        except:
            break

    return tar

ret = func([1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9])
print(ret)