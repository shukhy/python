# for  zip
person_name = ['shukhy','rahim','tuly','lamia']
person_age = [23,34,14,56]
gender = ['female','male','female','female']
department = ['IT','CSE','EEE','CSE']
result = ['A+','A','B+','A+']
combine_list = list(zip('1234',person_name,person_age,gender,result,department))
print(combine_list)
# for unzip#

for_unzip_list = [('1', 'p', 'shukhy', 23, 'female', 'A+', 'IT'), ('2', 'e', 'rahim', 34, 'male', 'A', 'CSE'), ('3', 'r', 'tuly', 14, 'female', 'B+', 'EEE'), ('4', 's', 'lamia', 56, 'female', 'A+', 'CSE')]
unzip = list(zip(*for_unzip_list))
print(unzip)

serial = unzip[0]
name = unzip[1]
age = unzip[2]
sex = unzip[3]
department = unzip[4]
result = unzip[5]

print( 'serial:',serial)
print('name:',name)
print('age:',age)
print('sex:',sex)
print('department:',department)
print('result:',result)

