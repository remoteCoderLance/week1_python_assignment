def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")

def get_operation():
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in valid_ops:
            return op
        print("Invalid operation. Please enter one of +, -, *, /.")

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return "Error: Division by zero" if b == 0 else a / b

# Main program
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = get_operation()

result = calculate(num1, num2, operation)
print(f"{num1} {operation} {num2} = {result}" if isinstance(result, (int, float)) else result)
