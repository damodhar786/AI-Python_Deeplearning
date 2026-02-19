# ## Pattern 7:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

print('-' * 65)

# ## Pattern 8

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = int(input("Enter a number: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end = " ")
    print()
print('-' * 65)


## Pattern 9

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

rows = int(input("Enter a number: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

