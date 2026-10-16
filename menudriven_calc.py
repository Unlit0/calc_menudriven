import math

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return round(a / b, 4)

def power(a, b):
    return round(a ** b, 4)

while True:
    print("\n==================================")
    print("       PYTHON CLI CALCULATOR")
    print("==================================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. View Calculation History")
    print("8. Clear History")
    print("9. Exit")

    ch = input("\nEnter your choice (1-9): ").strip()

    # options 1 to 5 need two numbers
    if ch in ["1", "2", "3", "4", "5"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("Invalid input! Please enter numbers only.")
            continue

        if ch == "1":
            res = add(num1, num2)
            record = f"{num1} + {num2} = {res}"
        elif ch == "2":
            res = subtract(num1, num2)
            record = f"{num1} - {num2} = {res}"
        elif ch == "3":
            res = multiply(num1, num2)
            record = f"{num1} * {num2} = {res}"
        elif ch == "4":
            res = divide(num1, num2)
            record = f"{num1} / {num2} = {res}"
        elif ch == "5":
            res = power(num1, num2)
            record = f"{num1} ^ {num2} = {res}"

        print("\nResult:", record)
        history.append(record)

    # square root only needs one number
    elif ch == "6":
        try:
            num = float(input("Enter number: "))
            if num < 0:
                print("Error! Cannot find square root of a negative number.")
            else:
                res = round(math.sqrt(num), 4)
                record = f"sqrt({num}) = {res}"
                print("\nResult:", record)
                history.append(record)
        except:
            print("Invalid input! Please enter a valid number.")

    elif ch == "7":
        print("\n--- Calculation History ---")
        if len(history) == 0:
            print("No calculations done yet.")
        else:
            for i in range(len(history)):
                print(f"{i + 1}. {history[i]}")

    elif ch == "8":
        history.clear()
        print("History cleared!")

    elif ch == "9":
        print("Closing calculator...")
        break

    else:
        print("Invalid choice! Please pick from 1 to 9.")