# Simple Calculator by Mdaib1

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error!"

print("--- Simple Calculator ---")
try:
    num1 = float(input("Lamba ta 1: "))
    op = input("Lissafi (+, -, *, /): ")
    num2 = float(input("Lamba ta 2: "))

    if op == '+': print(f"Sakamako: {add(num1, num2)}")
    elif op == '-': print(f"Sakamako: {subtract(num1, num2)}")
    elif op == '*': print(f"Sakamako: {multiply(num1, num2)}")
    elif op == '/': print(f"Sakamako: {divide(num1, num2)}")
    else: print("Babu wannan lissafin.")
except:
    print("Kuskure: Shigar da lamba kawai.")
