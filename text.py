l1 = [1, 2, 3, 4]
l2 = [2, 3, 4, 5]
l3 = list(zip(l1, l2))

print(l3)
for i in l3:
    print('for循环{}'.format(i))

l4 = [x for x in l3]
print(l4)

