## Name: Cory Strong
## Class: CSCI 101
## File Name : ShapeCalc_CStrong.py
## Description : This program is a simple ATM that allows a user to check their bank balance, deposit funds, and withdraw money.

def atm_system():
    balance = 1000.00

    def print_menu():
        print("Welcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    while True:
        print_menu()
        choice = input("Please select an option:").strip()

        if choice == "1":
            print("")
            print("*"*80)
            print(f"Your current balance is: ${balance:.2f}")
            print("*"*80)
            print("")
        elif choice == "2":
            print("")
            print("*"*80)
            deposit_amount = float(input("Enter deposit amount:").strip())
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"Deposit successful. Your new balance is: ${balance:.2f}")
                print("*"*80)
                print("")
            else:
                print("Deposit amount must be positive.")

        elif choice == "3":
            print("")
            print("*"*80)
            withdraw_amount = float(input("Enter withdrawal amount:").strip())
            if withdraw_amount > 0:
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
                    print("*"*80)
                    print("")
                else:
                    print("Insufficient funds. Withdrawal cannot be processed.")
                    print("*"*80)
                    print("")
            else:
                print("Withdrawal amount must be positive.")

        elif choice == "4":
            print("")
            print("")
            print(f"Thank you for using the ATM. Your final balance is: ${balance:.2f}")
            break
        else:
            print("")
            print("*"*80)
            print("Invalid option. Please select a valid option.")
            print("*"*80)
            print("")
atm_system()