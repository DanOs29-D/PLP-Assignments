# Get the first number from the user
num1_str = input("Please enter the first number: ")
num1 = float(num1_str)

# Get the second number from the user
num2_str = input("Please enter the second number: ")
num2 = float(num2_str)

# Get the desired operation from the user
operation = input("Please enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation entered. Please use +, -, *, or /.")