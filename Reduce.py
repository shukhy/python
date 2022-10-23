import functools
def add_value(n1 ,n2):
    return n1 + n2
list = [12,10,20,40,8,10]
result = functools.reduce(add_value,list)
print(result)