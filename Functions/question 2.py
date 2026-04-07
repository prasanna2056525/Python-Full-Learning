
def failpass_checker(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"
    
marks =int(input("Enter your marks: "))
result=failpass_checker(marks)
print(result)