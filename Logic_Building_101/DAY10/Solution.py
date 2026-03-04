# ## Pattern 1

# ```
# A
# B B
# C C C
# D D D D
# E E E E E
# ```

rows = int(input("Enter a number: "))

for i in range(rows):
    ch = chr(65 + i)

    for j in range(i + 1):
        print(ch, end = " ")
    print()
print("*" * 65)

#---------------------------------------------------------------------------------
## Pattern 2

# ```
#       A
#     A B A
#   A B C B A
# A B C D C B A
# ```

rows = int(input("Enter a number: "))

for i in range(rows):
    ch = chr(65 + i)

    for j in range(rows - i):
        print(" ", end = " ")
    
    for k in range(2 * i + 1):
        print(ch, end = " ")
    print()
print("*" * 65)
#---------------------------------------------------------------------------------

rows = int(input("Enter a number: "))

for i in range(rows):

    # spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")

    # increasing letters
    for j in range(i + 1):
        print(chr(65 + j), end=" ")

    # decreasing letters
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end=" ")

    print()
print("*" * 65)
#---------------------------------------------------------------------------------

# Write a program to swap two numbers entered by the user. For example:

# - **Input:** **`Enter first number: 10, Enter second number: 20`**
# - **Output:**

# ```
#     Before swapping: a = 10, b = 20
#     After swapping: a = 20, b = 10
# ```

a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a, b)
