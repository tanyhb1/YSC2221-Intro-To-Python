import numpy as np
from itertools import product
v1 = np.array([1,2,3])
v2 = np.array([4,9,16])
print(v1+v2)
print(v1*v2)
print(v1.dot(v2))
#for python, creating a multi-dimensional array initializes with the row first then column
c = np.zeros((3,5))
c[1][4] = 999
print(c)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
print(a[1:3,2:4])
print(a[:,0::2])
'''
np.matmul() for matrix multiplication. multiplying two matrixes in python is just an iterative multiplication, it doesn't
give you a matrix or dot product
'''
#boolean array indexing
bool_idx = (a>5)
print(bool_idx)
print(a[bool_idx])
#which is the same as saying,
print(a[a>5])
arr = [1,2,3,4]
arr_py = np.array(arr)
print(arr_py-5)


'''
if you want to loop through a 2d array, use data.shape
'''
arr2 = np.array([[1,2],[3,4],[5,6]])
