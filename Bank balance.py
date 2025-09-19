balance = 1000
print("Welcome to ATM")
print("1. Check Balance\n2. Deposit\n3. Withdraw")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Balance:", balance)
elif choice == 2:
    amt = int(input("Enter amount to deposit: "))
    balance += amt
    print("Updated Balance:", balance)
elif choice == 3:
    amt = int(input("Enter amount to withdraw: "))
    if amt <= balance:
        balance -= amt
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance")
