
amount = int(input("Enter the amount: "))

if amount >= 10000:
    print("You are eligible for a loan.")
elif amount >= 5000:
    print("You are eligible for a credit card.")
else:
    print("You are not eligible for any offer.")