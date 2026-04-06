days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print(days)

print(days[0])  # This will print the first element of the tuple, which is "Monday"
print(days[3])  # This will print the fourth element of the tuple, which is "Thursday"
print(days[-1])  # This will print the last element of the tuple, which is "Sunday"

'''
x= (1, 2, 3, 4, 5)
x[1] = 10  # This will raise a TypeError because tuples are immutable and cannot be modified after they are created
print(x)  # This line will not be executed due to the error in the previous line
'''

x= 1,
print(type(x))  # This will print the type of x, which is <class 'tuple'>, indicating that x is a tuple with a single element

