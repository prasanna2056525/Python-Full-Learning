
student ={}

student['id']=101
student['name']='John Doe'
student['age']=20
student['marks']=[85, 90, 78]
print(student)

student.update({'grade':'A'})
print(student)

#read only
'''
print(student['name'])
print(student.get('name'))

print(student.keys() )'''

for key, value in student.items():
    print(f"{key}: {value}")

del student['marks']
print(student)



