"""Write a program that keeps asking the user to enter a password until they
enter the correct one.
"""
password = input("Enter the password : ")
key = "123"

while password != key:
    password = input("Enter the correct password : ")

print("Password is correct")