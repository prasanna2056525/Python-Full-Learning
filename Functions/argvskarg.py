
def add(*numbers):
    Total = 0
    for i in numbers:
        Total += i
    return Total
result = add(10, 20, 30, 40,50,60,70,80,90,100)
print(result)


def user(name,age,city):
    print("Name:",name, "Age:",age, "City:",city)

user("Ram",25,"Kathmandu")


def user1(**details):
    print(details)

user1(name=["Ram","Shyam","Sita"],age=[25,30,22],city=["Kathmandu","Lalitpur","Bhaktapur"])

