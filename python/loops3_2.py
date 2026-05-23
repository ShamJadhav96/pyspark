"""Print the multiplication table of a number (entered by user)"""

num = int(input("Enter the number for which you want table  : "))
for i in range(1,11):
    print(num, "x", i , "=", num*i)