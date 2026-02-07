
# 1. **Program to Print Integer Numbers Entered by the User:**
#    Write a program where the user is asked to enter an integer number, and the program prints that number back to them. For example: 
#    - **Input:** **`42`**
#    - **Output:** **`You entered: 42`**

number = input("Enter your Lucky Number: ")

print("Your Lucky Number is: " + number)
print("--------------------------------------------------")

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. **Write a Program to Find the Size of `int`, `float`, `double`, and `char` on Your Computer:**
#    Write a program that displays the size of fundamental data types (**`int`**, **`float`**, **`double`**, and **`char`**) on your system. For example:
#    - **Output:**
#      ```python
#      Size of int: 28 bytes
#      Size of float: 24 bytes
#      Size of char: 41 byte

import sys
print(f"Size of int: {sys.getsizeof(int())} bytes")
print(f"Size of float: {sys.getsizeof(float())} bytes")
print(f"Size of string or character: {sys.getsizeof(str())} bytes")
print("--------------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. **Program to Find the Larger Number Among Two Numbers:**
#    Write a program to compare two integers entered by the user and print the larger one. For example:
#    - **Input:** **`Enter two numbers: 15, 20`**
#    - **Output:** **`The larger number is: 20`**

a = int(input("Enter 1st number: ") )
b = int(input("Enter 2nd number: "))

#  input function in python takes input as strings
if(a > b):
    print("The larger number is: " , a )
else:
    print("The larger number is: ", b)


