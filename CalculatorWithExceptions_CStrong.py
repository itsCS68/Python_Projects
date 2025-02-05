def calculate(op, num1, num2):

    try:
        num1 = float(num1)
        num2 = float(num2)

        if op == '+':
            return f"Result: {num1 + num2}"
        elif op == '-':
            return f"Result: {num1 - num2}"
        elif op == '*':
            return f"Result: {num1 * num2}"
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division by Zero.")
            return f"Result: {num1 / num2}"
        else:
            return "** Invalid operation. **"
    except ValueError:
        return "Error: Invalid input. Please enter valid numbers."
    except ZeroDivisionError as e:
        return f"Error: {e}"

def main():
    print("-"*40)
    print("{:^40}".format("Calculator With Exceptions"))
    print("-"*40)
    while True:
        op = input("Enter operation (+, -, *, /) or type 'exit' to quit: ").strip()
        if op.lower() == 'exit':
            print("Goodbye!")
            break

        num1 = input("Enter the first number: ").strip()
        num2 = input("Enter the second number: ").strip()

        result = calculate(op, num1, num2)
        print(result)

if __name__ == "__main__":
    main()