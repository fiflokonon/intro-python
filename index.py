def main():
    print("Basic Calculator")

    try:
        number1 = float(input("Input the first number: "))
        number2 = float(input("Input the second number: "))
        operation = input("Input an operation (+, -, *, /): ")

        if operation == '+':
            result = number1 + number2
            print(f"{number1} + {number2} = {result}")
        elif operation == '-':
            result = number1 - number2
            print(f"{number1} - {number2} = {result}")
        elif operation == '*':
            result = number1 * number2
            print(f"{number1} * {number2} = {result}")
        elif operation == '/':
            if number2 != 0:
                result = number1 / number2
                print(f"{number1} / {number2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operation.")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
