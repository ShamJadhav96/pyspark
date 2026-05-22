"""Write a program that asks the user for a number and prints whether it is
positive, negative, or zero."""

num = int(input("Please Enter the Number : "))

if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
elif num == 0:
    print(f"You provided zero")