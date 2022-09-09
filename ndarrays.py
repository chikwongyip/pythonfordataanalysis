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



