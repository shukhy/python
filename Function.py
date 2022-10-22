
def Mul_TwoNum(n1,n2):
    result = n1 * n2
    print(result)
Mul_TwoNum(3,6)

def Mul_Num(*num):
    result = 1
    for i in num:
        result=result*i
    print(result)
Mul_TwoNum(2,3,5,2)
