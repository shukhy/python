s1 = {1,2,3,4,5,6,7,8,9}
print(s1)
s2 = {2,3,15,13,10,11}
s1.update([16,19,20],s2)
print(s1)

#convert into list
print('convert into list')
s3 = list(set(s1))
print(s3)

#intersection between s1 and s2
print('intersection set')
s4 = s1.intersection(s2)
print(s4)

# set difference
print('set difference')
s5 = s1.difference(s2)
print(s5)

# symmetric_difference
print('symmetric_difference')
s6 = s1.symmetric_difference(s2)
print(s6)

# union set
s7 = s1.union(s2,s5)
print(s7)

# another way union set
print('union set')
s8 = s1|s2|s5
print(s8)