'''emails ={
    'john@example.com',
    'jane@example.com',
    'bob@example.com'
    'alice@example.com',
    'charlie@example.com',
    'bob@example.com',    
    'john@example.com'
}
print(emails)  # Output will show unique email addresses only'''

'''numbers = (1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10)

s= set(numbers)
print(s)  # Output will show unique numbers only

print(type(numbers))'''

#set operations
A = {1, 2, 3, 4, 5}
A.add(6)  # Adding an element to the set
print(A)  # Output: {1, 2, 3, 4,

A.remove(3)  # Removing an element from the set
print(A)  # Output: {1, 2, 4, 5, 6}
A.discard(2)  # Removing an element from the set (does not raise an error if the element is not present)
print(A)  # Output: {1, 4, 5, 6}


m={1, 2, 3}
n={3, 4, 5}

'''print(m.union(n))  # Output: {1, 2, 3, 4, 5}
print(m.intersection(n))  # Output: {3}
print(m.difference(n))  # Output: {1, 2}
print(m.symmetric_difference(n))  # Output: {1, 2, 4, 5}'''

print(m | n)  # Output: {1, 2, 3, 4, 5}
print(m & n)  # Output: {3}
print(m - n)  # Output: {1, 2}
print(m ^ n)  # Output: {1, 2, 4, 5}    

