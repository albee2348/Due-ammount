bill= float(input("Enter the bill amount: "))
paid= float(input("Enter the amount paid: "))

if paid < bill:
    bill-= paid
    print("You still owe: $", bill)
