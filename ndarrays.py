import numpy as np
# creating ndarrays
data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)

# 二维list 将会转换成 多维数组

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)

#arr2 有两个维度，我们可以确认通过

row = arr2.ndim
shape = arr2.shape

# 通过.type 可以知道narray的类型
type = arr1.dtype

#另外还可以通过zeros，ones和empty来创建 0， 1和空的数组
#传入的分别是(x,y,z)
np.zeros(10)
np.ones(20)
np.empty(2,3,1)

#指定data type 创建narray
arr1 = np.array([1,2,3], dtype=np.float64)

#你可以指定转换，或者CAST 一个数组用另外一种ndarray type 来定义
arr = np.array([1,2,3,4,5])

float_arr = arr.astype(np.float64)
#值得注意的是当你用numpy.string类型时候，data 类型是固定的，可能会截断

#如果casting fail 因为其他原因，ValueError will rasied
#数组是重要的，因为它们可以不需要循环来进行批量操作

arr = np.array([[1,2,3],[4,5,6]])
arr2 = arr * arr
arr0 = arr - arr

#Basic Indexing and Slicing（切片）

arr = np.arange(10)
#Slicing
arr[5]
# 还可以赋值
arr[5:8] = 12
#enumerate 函数
i = 0
for value in collection:
    i += 1

# for i, value in enumerate(collection):

# 索引数据，使用enumerate 映射到dict 上
some_list = ['foo','bar','baz']
mapping = {}

for i, v in enumerate(some_list):
    mapping[v] = i

# sorted 函数

sorted([7,1,2,6,0,3,2])
# 如果sorted 英文，则会拆开字母进行排序

sorted('horse  race')

# zip 函数
# 可以将多个列表，元组或其他序列成对组合一个元组列表
seq1 = ['foo','bar','baz']
seq2 = ['one','two', 'three']

zipped = zip(seq1,seq2)
list(zipped)
# 可以处理任意序列，元素的个数取决于最短序列
seq3 = [False,True]
list(zip(seq1,seq2,seq3))

# zip 最常见用法就是迭代多个序列

for i, (a,b) in enumerate(zip(seq1,seq2)):
    print('{0}:{1},{2}'.format(i,a,b))

#  给出一个被压缩得序列，zip 可以被用来解压序列，也可以当作，
# 把行的列转换列的列表

pitchers = [('Nolan','Ryan'),('Roger','Clemens'),
            ('Schilling','Curt')]
first_names, last_name = zip(*pitchers)

# reversed 函数
# 可以从后向向前迭代一个序列

list(reversed(range(10)))





