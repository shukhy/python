x = 100

def function_apple():
    y = x + 200
    print('inside value :',y)
    print(id(y))
function_apple()

print('outside value :', x)
print(id(x))

def function_orange():
    print('another inside value :',x)
    print(id(x))
function_orange()

def function_arithmetic():
    m = (x % 2)==0
    print('oh ! its even value :',m)
    n = (x % x) and (x % 1)
    print('its not prime number !',n)
function_arithmetic()