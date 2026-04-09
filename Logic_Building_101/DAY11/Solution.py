# 1. **Write a Program to Find the Largest Number Among Three Numbers:**

#    Write a program where the user enters three numbers, and the program finds and displays the largest number among them. For example:

#    - **Input:** **`Enter three numbers: 12, 25, 7`**
#    - **Output:** **`The largest number is: 25`**

a = int(input("Enter a 1st Number: "))
b = int(input("Enter a 2nd Number: "))
c = int(input("Enter a 3rd Number: "))



if a > b and a > c:
    print(f'The largest number is: {a}')
elif b > c and b > a:
    print(f'The largest number is: {b}')
else:
    print(f'The largest number is: {c}')

print("-" * 65)

print(f'The largest number is: {max(a,b,c)}')

print("-" * 65)

# ----------------------------------------------------------------------------------------------------------

# 2. **Write a Program to Check Whether a Year Entered by the User is a Leap Year:**

#    Write a program to determine whether a given year is a leap year. For example:

#    - **Input:** **`Enter a year: 2024`**
#    - **Output:** **`2024 is a leap year.`**
# (Year % 4 == 0 AND Year % 100 != 0) OR (Year % 400 == 0)



def leap_year_or_not(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year} is a LEAP YEAR')
    else:
        print(f'{year} NOT a LEAP YEAR')

year = int(input("Enter a Year: "))
leap_year_or_not(year)

print("-" * 65)

# ----------------------------------------------------------------------------------------------------------

# 3. **Write a Program to Calculate the Sum of the First N Natural Numbers:**

#    Write a program where the user enters a number **`N`**, and the program calculates the sum of all natural numbers up to **`N`**. For example:

#    - **Input:** **`Enter a number: 5`**
#    - **Output:** **`The sum of the first 5 natural numbers is 15.`**

def first_n_natural_number(number):
    total = 0
    for n in range(number):
        total += (n + 1)
    print(f'Sum of the First N Natural Numbers: {total}')
    
first_n_natural_number(int(input("Enter a Number: ")))





