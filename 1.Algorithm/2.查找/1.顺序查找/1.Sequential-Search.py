seq = [9,8,7,6,5,4,3,2,1,0,-1,-7,-6,-5,-4,-3,-2]
tar = 511

def sequential_search():
    for num in seq:

        if num == tar:

            return num
    return None

print(sequential_search())
