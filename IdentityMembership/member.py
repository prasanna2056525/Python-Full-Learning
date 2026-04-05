

student = ["Alice", "Bob", "Charlie", "David", "Eve"]

print ("Alice" in student) # This is a membership operator that checks if the value "Alice" is present in the list "student" and returns True if it is, otherwise it returns False
print ("Frank" in student) # This is a membership operator that checks if the value "Frank" is present in the list "student" and returns True if it is, otherwise it returns False
print ("Charlie" not in student) # This is a membership operator that checks if the value "Charlie" is not present in the list "student" and returns True if it is not, otherwise it returns False
print ("Grace" not in student) # This is a membership operator that checks if the value


allowed_users = [ "admin", "user1", "user2", "user3"]
username = input("Enter your username: ")
if username in allowed_users: # This is a membership operator that checks if the value of "username" is present in the list "allowed_users" and returns True if it is, otherwise it returns False
    print("Access granted")
else:
    print("Access denied")