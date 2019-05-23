

# 无序列表
# 空间复杂度O(1)

def func(tar):

    for i,num in enumerate(tar):

        for j,foo in enumerate(tar[i+1:]):

            print(num,foo)
        print("----")



    return tar

ret = func([1, 1, 1, 2, 1,2,8,4,2,22,3,2, 2,])
print(ret)