
amount = int(input("Enter the amount: "))

if amount>= 10000:
    print("You are eligible for a 10% discount.")
    mode= input("A-CASH, B-CREDIT CARD, C-DEBIT CARD: ")
    if mode == "A":
        print("You can pay in cash and get the discount.")
    elif mode == "B" or mode == "C":
        print("You can pay with a credit or debit card and not eligible to get the discount.")
    else:
        print("Invalid payment mode.")
        
elif amount >= 5000:
    print("You are eligible for a 5% discount.")
    mode= input("A-CASH, B-CREDIT CARD, C-DEBIT CARD: ")
    if mode == "A":
        print("You can pay in cash and get the discount.")
    elif mode == "B" or mode == "C":
        print("You can pay with a credit or debit card and not eligible to get the discount.")
    else:
            print("Invalid payment mode.")
else:
    print("You are not eligible for any discount.")