"""Use a while loop to reverse a given number (e.g., 123 → 321)"""

num = int(input("Enter the number : "))
reverse = 0

while num != 0:
    digit = num % 10
    reverse = digit + reverse*10
    num = num // 10 
print("Reverse number is : " , reverse)
