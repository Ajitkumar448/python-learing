balance = 1000


def check_balance():
    global balance
    print("Your current balance is:", balance)


def withdraw_money():
    global balance

    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient balance")

    elif amount <= 0:
        print("Enter a valid amount")

    else:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)


def deposit_money():
    global balance

    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Enter a valid amount")

    else:
        balance += amount
        print("Deposit successful")
        print("Updated balance:", balance)


def atm_menu():

    while True:

        print("\n===== MINI ATM =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            withdraw_money()

        elif choice == 3:
            deposit_money()

        elif choice == 4:
            print("Thank you for using the ATM")
            break

        else:
            print("Invalid choice")


# Start ATM
atm_menu()