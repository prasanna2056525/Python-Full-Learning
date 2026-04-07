
def count_even_numbers(n):
    count=0
    for i in range(1,n+1):
        if i%2==0:
            print(i)
            count+=1    
    return count
n=int(input("Enter a number: "))
result=count_even_numbers(n)
print(f"The number of even numbers between 1 and {n} is:",result)
