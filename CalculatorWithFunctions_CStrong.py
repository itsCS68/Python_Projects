## Name: Cory Strong
## Class: CSCI 101
## File Name: CalculatorWithFunctions_CStrong.py
## Program that acts as simple a calculator, prompting users to input numbers and operations.

def main():
    welcomeMessage()
    last_result = None

    while True:
        if last_result is None:
            num1 = get_number("What's your number?: ")
        else:
            use_last = input(
                f"Do you want to use the last result ({last_result}) as the first number? (y/n): ").strip().lower()
            if use_last in ['yes', 'y']:
                num1 = last_result
            else:
                num1 = get_number("What's your number?: ")
        print("+")
        print("-")
        print("*")
        print("/")

        choice = input("Choose an operation: ").strip().lower()

        if choice not in ['+', '-', '*', '/']:
            print(f"Invalid operation. Please try again.")
            continue

        if choice == '/':
            num2 = nonZeroNumber("What's the next number?: ")
        else:
            num2 = get_number("What's the next number?: ")

        if choice == '+':
            last_result = addition(num1, num2)
            print(f"The result of addition is: {num1} + {num2} = {last_result:.1f}")
        elif choice == '-':
            last_result = subtraction(num1, num2)
            print(f"The result of subtraction is: {num1} - {num2} = {last_result:.1f}")
        elif choice == '*':
            last_result = multiplication(num1, num2)
            print(f"The result of multiplication is: {num1} * {num2} = {last_result:.1f}")
        elif choice == '/':
            last_result = division(num1, num2)
            print(f"The result of division is: {num1} / {num2} = {last_result:.1f}")


def welcomeMessage():
    print("*" * 40)
    print("{:^40}".format("PyCalcula!"))
    print("*" * 40)

def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid number.")


def nonZeroNumber(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number != 0:
                return number
            print("The number cannot be zero. Please try again.")
        except ValueError:
            print(f"Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()




