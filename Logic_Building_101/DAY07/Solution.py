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
    print(f"i = {i}")
    for j in range(i):
        print(f"j = {j}", end = " ")        
    print()