# 1. **Print the Multiplication Table of a Given Number:**

#    Write a program where the user enters a number, and the program prints its multiplication table. For example:

#    - **Input:** **`Enter a number: 5`**
#    - **Output:**
#      ```jsx
#      5 x 1 = 5
#      5 x 2 = 10
#      ...
#      5 x 10 = 50
#      ```

num = int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

print("-" *  65)


# 2. **Write a Program to Make a Simple Calculator**

#    Write a program that acts as a calculator, taking two numbers and an operator 
#   (**`+`**, **`-`**, **`*`**, **`/`**) from the user, and performing the operation based on the operator. For example:

#    - **Input:** **`Enter first number: 10, Operator: +, Second number: 20`**
#    - **Output:** **`10 + 20 = 30`**

n1 = float(input("Enter first Number: "))
n2 = float(input("Enter Second Number: "))
operator = input("Select an Operator ** + **, ** - **, ** * **, ** / **:    ")


if operator == "+":
    sum = n1 + n2
    print(f"Output: {n1} + {n2} = {sum}")
elif operator == "-":
    subtraction = n1 - n2
    print(f"Output: {n1} - {n2} = {subtraction}")
elif operator == "*":
    multiplication = n1 * n2
    print(f"Ouput: {n1} * {n2} = {multiplication}")
elif operator == "/":
    division = n1 / n2
    print(f"Output: {n1} / {n2} = {division}")

print("-" *  65)


# 3. **Print a Number in Reverse Order:**

#    Write a program where the user enters a number, and the program prints it in reverse order. For example:

#    - **Input:** **`1234`**
#    - **Output:** **`4321`**

num1 = int(input("Enter a number: "))
reverse = 0
while num1 > 0:
    last_digit = num1%10
    print(f"last digit:  {last_digit}")
    reverse = (reverse * 10) + last_digit
    print(f"reverse: {reverse} ")
    num1 = num1//10
    print(num1)
    print("*" * 10)
print(f"Reversed Number: {reverse}")

# print("-" * 65)


