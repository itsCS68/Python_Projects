## Name: Cory Strong
## Class: CSCI 101
## File Name : PasswordGenerator_CStrong.py
## Description : This code prompts users to select certain variables which then computes a password that appears
## complex.

Header = "Password Generator"
print('-'*30)
print(Header.center(30))
print('-'*30)
print("Welcome to the PyPassword Generator!")
print("")
import random
import string


def generate_password(num_letters, num_symbols, num_numbers):
    letters = list(string.ascii_letters)
    symbols = list('*%*!&)(@')
    numbers = list(string.digits)

    # Use random.choices to allow repetition if more symbols/numbers are requested than available
    password_letters = random.choices(letters, k=num_letters)
    password_symbols = random.choices(symbols, k=num_symbols)
    password_numbers = random.choices(numbers, k=num_numbers)

    # Combine all parts and shuffle
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    return ''.join(password_list)


def main():
    try:
        num_letters = int(input("How many letters would you like in your password? "))
        num_symbols = int(input("How many symbols would you like? "))
        num_numbers = int(input("How many numbers would you like? "))

        # Check if the inputs are valid (positive integers)
        if num_letters < 0 or num_symbols < 0 or num_numbers < 0:
            print("Please enter positive numbers only.")
            return

        password = generate_password(num_letters, num_symbols, num_numbers)
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
