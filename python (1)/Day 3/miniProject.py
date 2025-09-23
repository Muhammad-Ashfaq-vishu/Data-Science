balance = 1000

def show_menu():
    print("\nATM Machine Simulation\n")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    global balance
    print("Your current balance is:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit Successful. Your new balance is:", balance)

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal Successful. Your new balance is:", balance)

while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
