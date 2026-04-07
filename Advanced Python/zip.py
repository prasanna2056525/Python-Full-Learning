names = ['Ram', 'Shyam', 'Hari' ,'Sita', 'Gita']

marks = [85, 90, 78, 92, 88]

for i in range(len(names)):
    print(names[i], marks[i])

for name, mark in zip(names, marks):
    print(name, mark)