# 17. Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator.
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    if y == 0:
        return "Cannot be divide by zero"
    else:
        return x/y


print("Choose operator: ")
print("1. +")
print("2. -")
print("3. /")
print("4. *")

while True:
    choice = int(input("Enter operator number:"))

    if choice in (1, 2, 3, 4):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == 1:
            print(x, "+", y, "=", add(x, y))

        elif choice == 2:
            print(x, "-", y, "=", subtract(x, y))

        elif choice == 3:
            print(x, "*", y, "=",  multiply(x, y))

        elif choice == 4:
            print(x, "/", y, "=",  divide(x, y))
        break
    else:
        print('Invalid choice')






