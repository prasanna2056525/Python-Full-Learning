my_list = [1, 2, 3, 4, 5]  # This is a list of integers from 1 to 5

my_list.append(6)  # This will add the number 6 to the end of the list
print(my_list)  # This will print the updated list, which now includes the number 6

new_list = [7, 8, 9]  # This will create a new list by concatenating the original list with another list containing the numbers 7, 8, and 9
my_list.append(new_list)

print(my_list)  # This will print the original list, which now includes the new list as its last element


a=[1, 2, 3]
b=[4, 5, 6]
a.extend(b)  # This will add the list b as a single element to the end of the list a
print(a)  # This will print the updated list a, which now includes the list b

c=[]
c.extend("hello")
print(c)  # This will print the list c, which now contains the individual characters of the string "hello" as separate elements


d= [1,2,3,4,5,6,7,8,9,10]

d.insert(2,90)
d.remove(5)  # This will remove the first occurrence of the number 5 from the list d    

print(d)  # This will print the updated list d, which now includes the number 90 at index 2

g = ["apple", "banana", "cherry", "date", "fig", "grape"]
print('before removing:', g)  # This will print the original list g before removing any elements
g.remove("date")  # This will remove the first occurrence of the string "date" from the list g
print('after removing:', g)  # This will print the updated list g after removing the string "date"


y =[10,20,30,40,50]

x= y.pop(3)  # This will remove and return the element at index 3 from the list y, which is 40
print(x)  # This will print the value of x, which is 40
print(y)  # This will print the updated list y, which now contains [10, 20, 30, 50]

print(x+100)  # This will add 100 to the value of x (which is 40) and print the result, which is 140


markss = [85, 90, 78, 92, 88]
markss.sort()  # This will sort the list markss in ascending order
print(markss)  # This will print the sorted list markss, which is now [

markss.sort(reverse=True)  # This will sort the list markss in descending order
print(markss)  # This will print the sorted list markss, which is now [


n = [3, 1, 4, 1, 5, 9]
n.count(1)  # This will count the number of occurrences of the number 1 in the list n, which is 2
print(n.count(1))  # This will print the count of the number 1 in the list n, which is 2
