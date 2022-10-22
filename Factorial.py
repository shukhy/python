# find out factorial number using function

def fact(x):
    initial = 1
    for i in range(1, x+1):
        initial*=i
    return initial
result = fact(5)
print(result)

# another way

number = int(input('enter any number:'))
f = 1
for i in range(1, number+1):
    f = f * i
print(f)



