

def fact(number):

   if number == 1:
    return 1
   else:
     return number * fact(number-1)
result = fact(5)
print(result)
