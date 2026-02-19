# ## Pattern 1: Inverted Right-angled triangle

# ```
# * * * * *
# * * * *
# * * *
# * *
# *
# ```

rows = int(input("Enter a number: "))

for i in range(rows, 0, -1):
    
    for j in range(i):
        print("*", end = " ")        
    print()

print("-" * 65)
#-------------------------------------------------------------------------------------

# ## Pattern 2: traingle

# ```
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# ```

rows = int(input("Enter a number: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end = " ")

    for k in range(2 * i - 1):
        print("*", end = " ")
    print()

print("-" * 65)

#-----------------------------------------------------------------------------------

rows = int(input("Enter a number: "))

for i in range(1, rows + 1):
    
    for j in range(i - 1):
        print(" ", end = " ")
    
    # print stars
    for k in range(2 * (rows - i) + 1):
        print("*", end = " ")

    print()