'''numbers = [1, 2, 3, 4, 5]
squares=[]
for i in numbers:
    square= i*i
    squares.append(square)
print(squares)'''

numbers = [1, 2, 3, 4, 5]
squares = [i*i for i in numbers]
print(squares)