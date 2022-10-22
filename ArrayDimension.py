from numpy import *
array1 = array([
    [2,3,4,5,6,7],
    [1,3,5,7,9,2]
])
print(array1)
print(array1.dtype)
print(array1.ndim)
print(array1.shape)

array2 = array1.reshape(3,4)
print(array2)
print(array2.dtype)
print(array2.ndim)
print(array2.shape)

array3 = array1.flatten()
print(array3)
print(array3.dtype)
print(array3.ndim)
print(array3.shape)

array4 = array1.reshape(2,2,3)
print(array4)