import numpy as np
data ={i: np.random.randn() for i in range(7)}
# print(data)

# 元组
tup = 4, 5, 6
print(tup)

tup1 = tuple([0,1,2,3])
print(tup1)
print(tup1[0])
print(tup1[2])
# tup1[0] = 1 # 元组对象不能改变
# tup1[0].append(1)
# 元组相加
tup2 = tup1 + tup
# 元组相乘
tup3 = tup1 * 2

# 拆分元组
a, b, c, d = tup1

# 列表 list

a_list = [2, 3, 7, None]

b_list =list(tup)
b_list[2] = 0
b_list.insert(0,"happy")

