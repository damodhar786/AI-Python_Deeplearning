# 1. **Factorial of a Number Using a For Loop:**

#    Write a program to calculate the factorial of a number entered by the user using a **`for`** loop. For example:

#    - **Input:** **`Enter a number: 4`**
#    - **Output:** **`Factorial of 4 is 24.`**

num = int(input("Enter a Number: "))

f = 1

if num < 0:
    print(f'The Factorial of NEGATIVE number is not Determined')
else:
    for n in range(1, num + 1):
         f *= n 
    print(f'Factorial of {num} is {f}')

print("-" * 65)

#-------------------------------------------------------------------------------------------------

# 2. **Print Fibonacci Series:**

#    Write a program to print the Fibonacci series up to a number **`N`** entered by the user. For example:

#    - **Input:** **`Enter the number of terms: 7`**
#    - **Output:** **`Fibonacci series: 0 1 1 2 3 5 8`**

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = ' ')
        a, b = b, a + b

fibonacci(int(input("Enter a Number: ")))

print("-" * 65)

#-------------------------------------------------------------------------------------------------

# 3. **Write a Program to Find the GCD or HCF of Two Numbers:**

#    Write a program where the user enters two numbers, and the program calculates their greatest common divisor (GCD) or highest common factor (HCF). For example:

#    - **Input:** **`Enter two numbers: 60, 48`**
#    - **Output:** **`The GCD of 60 and 48 is 12.`**

def gcd(a, b):
    x, y = a, b
    while b:
        a , b = b, a % b
    print(f'The GCD or HCF of {x} & {y} is {a}')

n1 = int(input("Enter a number 1: "))
n2 = int(input("Enter a number 2: "))

gcd(n1, n2)
