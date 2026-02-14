# 1. **Calculate the Sum of Digits of a Given Number:**

#    Write a program that calculates the sum of the digits of a number entered by the user. For example:

#    - **Input:** **`Enter a number: 1234`**
#    - **Output:** **`Sum of digits: 10`**

# number = int(input("Enter a Number"))
# original_number = number
# sum = 0

# if number > 0:
#     while number > 0:
#         last_digit = number % 10
#         sum = sum + last_digit
#         number = number // 10

# print(f"Sum of digits {original_number} = {sum} ")

number = input("Enter a Number")
sum = 0

for digit in number:
    sum = sum + int(digit)

print(f"Sum of digits {number} = {sum} ")

print("-" * 65)

#------------------------------------------------------------------------------------

# 2. **Write a Program to Check Whether a Character is a Vowel or Consonant:**

#   Write a program to check whether a character entered by the user is a vowel (**`a, e, i, o, u`**) or a consonant. 
#   For example:

#    - **Input:** **`Enter a character: e`**
#    - **Output:** **`e is a vowel.`**

vowels = ["a", "e", "i", "o", "u"]
character = input("Enter a Character: ").lower()

if character in vowels:
    print(f"{character} is a Vowel")

else:
    print(f"{character} is a Consonant")

print("-" * 65)

#------------------------------------------------------------------------------------

# 3. **Write a Program to Find the ASCII Value of a Character:**

#    Write a program that takes a character as input and displays its ASCII value. For example:

#    - **Input:** **`Enter a character: A`**
#    - **Output:** **`ASCII value of A: 65`**

character = input("Enter a Character: ")

ascii_value = ord(character)

print(f"ASCII value of {character} is {ascii_value}")


