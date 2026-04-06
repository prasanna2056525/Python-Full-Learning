
a = [1,2,[3,4]]

b= a.copy()  # This creates a shallow copy of the list 'a' and assigns it to 'b'
b[2].append(5)  # This will modify the inner list [3, 4] in both 'a' and 'b' because they reference the same inner list
print(a)  # This will print the original list 'a', which now includes the modified
print(b)  # This will print the copied list 'b', which also includes the modified inner list


# deep copy 

import copy
a = [1,2,[3,4]]
b = copy.deepcopy(a)  # This creates a deep copy of the list 'a' and assigns it to 'b'
b[2].append(5)  # This will modify the inner list [3, 4] in 'b' only, because 'a' and 'b' reference different inner lists
print(a)  # This will print the original list 'a', which remains unchanged
print(b)  # This will print the copied list 'b', which includes the modified inner list
