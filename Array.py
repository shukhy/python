from array import *

amount = array('i',[3555,2333,5666,7888,9666])
print('print first amount')
print(amount[0])
print('All amount:')
for i in range(5):
   print(amount[i])
print(amount.buffer_info())
print(amount.reverse())
print(amount)
print(amount.append(4000))
print(amount)
print(amount.remove(2333))
print(amount)