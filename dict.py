# 字典
# 字典可能是python 最重要的数据结构，它更为常见的名字是哈希映射，或者关联数组
# 定义
empty_dict = {}

d1 = {'a': 'some value','b':[1,2,3,4]}
#  插入
d1[7] = "nice"

#访问
d1['a']

# 检查列表和元组是否包含某个值的方法，检查字典中是否包含某个键
'b' in d1 

# 可以用del 关键字或pop 方法来删除值
del d1['a']

# ret 是pop 的返回值
ret = d1.pop('a')

# keys 和 values 是字典和值的迭代器方法
list(d1.keys())
list(d1.values())

#update 用一个字典与另外一个字典融合
# 如果是键相同，对应的value 将会update
d1.update({'b':"foo",'c':"some"})

# 用序列创建字典
mapping = {}
# for key, value in zip(key_list,value_list):
#     mapping[key] = value
mapping = dict(zip(range(5)),reversed(range(5)))
# 默认值

# if key in some_dict:
#     value = some_dict[key]
# else:
#     value = default_value

# value = some_dict.get(key, default_value)

words = ['apple','bat','bar','atom','book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

for word in words:
    letter = word[0]
    by_letter.setdefault(letter,[]).append(word)

# 有效键类型
# 键通常是不可变得标量类型，可以用hash 函数来检测一个对象是否可哈希
hash('string')

