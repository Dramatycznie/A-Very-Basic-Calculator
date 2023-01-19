def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

running = True
while running:
    print("Hello, I am the calculator. How can I help you?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    if not choice.isdigit() or int(choice) not in range(1, 6):
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    else:
        choice = int(choice)
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == 5:
        print("Thank you for using the calculator. Goodbye! ")
        running = False