d1 = {'name':'shukhy','age':23,'gender':'female'}
d2 = {'sur name':'akter','study':'bsc',10.5:10.5,True:True,(2,3):67}
print(d2)
#tuple value print
print(d2[2,3])
#add into d1
d1['versity']=['southeast university']
print(d1)
#delete into d2
d2.pop('sur name')
print(d2)
#key
print(d1.keys())
#items
print(d2.items())
#get value
print(d1.get('age'))

# for nested_dictionary

employee = {1:{'name':'Malek mia','age':45,'department':'IT'},
            2:{'name':'Shohel rana','age':49,'department':'HR'},
            3:{'name':'Asraf bhua','age':55,'department':'ACCOUNT'},
            4:{'name':'Babul borman','age':53,'department':'MANAGEMENT'},
            5:{'name':'Ellen alex','age':44,'department':'APPENDICS'}
            }
print(employee)
print(employee[2])
print(employee[1]['department'])
print(employee[3]['department'])
print(employee[5]['name'])

# update
employee[1]={}
employee[1]['name']='Nadim nakir'
employee[1]['age']=50
print(employee[1])
print(employee)

#delete
del employee[2]['department']
print(employee[2])
print(employee)
