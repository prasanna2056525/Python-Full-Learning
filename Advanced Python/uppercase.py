
'''names =['Ram', 'Shyam', 'Hari' ,'Sita', 'Gita']

result =[name.upper() for name in names]

for name in names:
    result.append(name.upper())
print(result)'''


class1=[ 'Python', 'Java', 'C++', 'JavaScript']

for i in range(len(class1)):
    print(i, class1[i])

for index,name in enumerate(class1,start=1):
    print(index, name)  