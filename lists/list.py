ages = [25, 30, 35, 40, 45]  # This is a list of ages that contains five integer values
print(ages)  # This will print the entire list of ages

print(ages[0])  # This will print the first element of the list, which is 25
print(ages[2])  # This will print the third element of the list, which
print(ages[-1])  # This will print the last element of the list, which is 45
ages[1] = 31  # This will change the second element of the list from 30 to 31

total = sum(ages)  # This will calculate the sum of all the ages in the list
print("The total of all ages is:", total)  # This will print the total of all ages
average = total / len(ages)  # This will calculate the average age by dividing the total by the number of ages in the list
print("The average age is:", average)  # This will print the average age        

for age in ages:
    total_sum = ages[0] + ages[1] + ages[2] + ages[3] + ages[4]
print("The total sum of ages is:", total_sum)  # This will print the total sum of ages calculated using a for loop
