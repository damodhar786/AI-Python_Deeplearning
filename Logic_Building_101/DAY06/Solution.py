# ## Pattern 1: Sqaure

# ```
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# ```


# rows = int(input("Enter a number: "))

# for i in range(rows):
#     for j in range(rows):
#         print("*", end = "")
#     print()

# print("-" * 65)

#------------------------------------------------------------------------------------------

# ## Pattern 2: Right-angled trinagle

# ```
# *
# * *
# * * *
# * * * *
# * * * * *
# ```

rows = int(input("Enter a number: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end = "")         
    print()


print("-----------------------------")


# ## Pattern 3: Hallow Rectangle

# ```
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# ```

rows = int(input("Enter a Rows number: "))
cols = int(input("Enter a Cols Number: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()