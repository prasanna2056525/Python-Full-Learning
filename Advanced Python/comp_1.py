
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [i for i in numbers if i % 2 == 0]
print(even)

even1=[ "even"  if i % 2 == 0 else "odd" for i in numbers]
print(even1)
        