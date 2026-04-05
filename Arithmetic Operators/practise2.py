
# Total bill with Tax

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
tax_rate = 13

subtotal = price * quantity
tax = subtotal * (tax_rate / 100)
total_bill = subtotal + tax

print("Subtotal: $", subtotal)
print("Tax: $", tax)
print("Total Bill: $", total_bill)

