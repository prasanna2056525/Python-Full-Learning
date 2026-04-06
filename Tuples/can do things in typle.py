x =(1,2,3,4,5,3,4,5,1,1,1,1,1,1,1,1,1,1,1,1,1)  

for a in x:
    print(a)  # This will print each element of the tuple x on a new line, including duplicates

print(x.count(1))  # This will count the number of occurrences of the number 1 in the tuple x, which is 14
print(x.index(3))  # This will return the index of the first occurrence of the number 3 in the tuple x, which is 2
