# DAY - 02

# 1. **Program to Check Whether the Number is Odd or Even:**

#    Write a program that checks whether a number entered by the user is odd or even. For example:

#    - **Input:** **`Enter a number: 7`**
#    - **Output:** **`7 is an odd number`**

number = int(input("Enter a number: "))
if (number % 2 == 1):
    print(f"""{number} is an Odd Number""")
else:
    print(f"""{number} is an Even Number""")

print("---------------------------------------------------------------")


#------------------------------------------------------------------------------------------------------

# 2. **Program to Check Whether the Number is Divisible by 5:**

#    Write a program that determines if a number entered by the user is divisible by 5. For example:

#    - **Input:** **`Enter a number: 25`**
#    - **Output:** **`25 is divisible by 5.`**

divNum = int(input("Enter a number: "))
if (divNum % 5 == 0):
    print(f"{divNum} is divisible by 5")
else:
    print(f"{divNum} is not divisible by 5")

print("---------------------------------------------------------------")

#------------------------------------------------------------------------------------------------------
# 3. **Program to Check Whether the Number is a Multiple of 7:**

#    Write a program that verifies if a number entered by the user is a multiple of 7. For example:

#    - **Input:** **`Enter a number: 14`**
#    - **Output:** **`14 is a multiple of 7.`**

mulNum = int(input("Enter a number: "))
if (mulNum % 7 == 0):
    print(f"""{mulNum} is Multiple of 7""")
else:
    print(f"""{mulNum} is not Multiple of 7""")

print("---------------------------------------------------------------")