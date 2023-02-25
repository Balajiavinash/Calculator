# Define the main function to perform arithmetic operations
def calculator():
    # Prompt user for input and convert it to a float
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user for operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform operation and print result
    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 == 0:
            print("Error: division by zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operation")

# Call the calculator function to run the program
calculator()
