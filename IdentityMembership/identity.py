a=10
b=10    
print(a is b) # This is an identity operator that checks if two variables refer to the same object in memory and returns True if they do, otherwise it returns False

c = [1, 2, 3]
d = [1, 2, 3]

print(c is d) # This is an identity operator that checks if two variables refer to the same object in memory and returns True if they do, otherwise it returns False

e=10
f=100

print(e is not f) # This is an identity operator that checks if two variables do not refer to the same object in memory and returns True if they do not, otherwise it returns False