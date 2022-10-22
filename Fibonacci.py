#0,1,1,2,3,5,8..............
def fibo(n):
    a = 0
    b = 1
    print(0)
    print(1)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fibo(10)