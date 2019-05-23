def func(tar):
    tar_copy = []
    for foo in tar:
        if foo not in tar_copy:
            tar_copy.append(foo)
    return tar_copy
ret = func([1,2,2,2,2,3,4,5,6,7,8,9,8,1,2,3,4])
print(ret)