import re

#定义了两个group,因为包含两个括号
m = re.search("(\w+) (\w+)", "Isaac Newton, physicist")

# #group(0)就是匹配的整个结果
# print(m.group(0))                           #输出结果为Isaac Newton
#
# #group(1)是第一个group的值
# print(m.group(1))                           #输出结果为Isaac
#
# #group(2)是第二个group的值
# print(m.group(2))                           #输出结果为Newton


#groups返回所有的group,以元组的形式
print(m.groups())                           #输出结果为('Isaac','Newton')