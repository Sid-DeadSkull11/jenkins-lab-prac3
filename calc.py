import sys

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        sys.exit(1)
    return a / b

if __name__ == "__main__":
    # Validate that all required arguments are passed
    if len(sys.argv) < 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        print("Operations: add, sub, mul, div")
        sys.exit(1)

    operation = sys.argv[1].lower()
    
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Inputs must be valid numbers.")
        sys.exit(1)

    # Execute the requested operation
    if operation == "add":
        print(f"Result: {add(num1, num2)}")
    elif operation == "sub":
        print(f"Result: {subtract(num1, num2)}")
    elif operation == "mul":
        print(f"Result: {multiply(num1, num2)}")
    elif operation == "div":
        print(f"Result: {divide(num1, num2)}")
    else:
        print(f"Error: Invalid operation '{operation}'")
        sys.exit(1)
