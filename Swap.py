a = 3444
b =10000

temp = a
a = b
b = temp
print('a = ',a)
print('b = ',b)

# another way
a,b = b,a
print('another way:')
print('a = ',a)
print('b = ',b)