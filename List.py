list = [1,['shukhy',2.3,7],2,3,'shukhy org',7,7]
print(list)
list.extend([3.3,4.4,5,5])
print(list)
print(list[1][0])

list.remove('shukhy org')
print(list)
print(list.count(7))
