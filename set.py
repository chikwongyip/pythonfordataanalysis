# 集合
# 集合是无序的不可重复的元素集合
# 创建 会把相同的删除
from msilib.schema import Condition


set([2,3,4,5,6,2])

{2,3,2,2,1}

# 支持合并,交集，差分和对称差数学集合运算

a = {1,2,3,4,5}
b = {3,4,5,6,7}
#并集
a.union(b)
a | b
# 交集
a.intersection(b)
a & b
# 可以直接用结果替代集合内容，对于大的集合，这么做效率更高
c = a.copy()
c | b

# 集合元素通常是不可变的，要获得类似列表的元素，必须转换元组
my_data = [1,2,3,4]
my_set = {tuple(my_data)}
# 检测一个集合是否另一个集合的子集或者父集
a_set = {1,2,3,4,5}
{1,2,3}.issubset(a_set)

a_set.issuperset({1,2,3})

# 集合内容相同时

a = {1,2,3}
b = {3,2,1}
a == b

# 列表，集合和字典推导式
result = []
# for val in collections:
#     if condition:
#         result.append(expr)

strings = ['a','as','bat','car','dove','python']
upper_string = [x.upper() for x in strings if len(x) > 2]
