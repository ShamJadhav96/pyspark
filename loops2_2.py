"""Write a program using match case that simulates a simple calculator.
Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case.
"""

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
operation = input("Enter the operation (+, -, *, /) : ")

match operation:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        if b == 0:
            print("Divide will not happen as b is o")
        else:
            print(int(a/b))