"""Write a program that takes a number from the user and prints “Even” if it is
even, otherwise “Odd”.
"""

N = int(input("Enter the number : "))

if N%2 == 0:
    print(f"{N} is Even number")
else:
    print("You enterd odd number")