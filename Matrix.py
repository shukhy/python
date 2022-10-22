import numpy as np

matrix1 = (
    [10,20,30,40],
    [20,10,30,20],
    [50,60,90,70]
)
matrix2 = (
    [90,20,30,40],
    [80,10,30,20],
    [70,60,90,70]
)
print('matrix1:')
print(matrix1)
print('matrix2:')
print(matrix2)

print('matrix addition:')
result1 = np.add(matrix1,matrix2)
print(result1)

print('matrix subtruction:')
result2 = np.subtract(matrix1,matrix2)
print(result2)

print('matrix multiplication:')
result3 = np.multiply(matrix1,matrix2)
print(result3)