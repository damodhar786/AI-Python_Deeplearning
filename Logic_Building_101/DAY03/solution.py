# # DAY - 03

# 1. **Program to Calculate the Square and Cube of a Number:**

#    Write a program where the user enters a number, and the program calculates its square and cube. For example:

#    - **Input:** **`Enter a number: 3`**
#    - **Output:** **`Square: 9, Cube: 27`**

number = int(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print(f"Square: {square}, Cube: {cube}")
print("-" * 63)

#---------------------------------------------------------

# 2. **Program to Calculate the Area of a Circle and Triangle:**

#    Write a program to calculate the area of a circle given its radius and a triangle given its base and height. For example:

#    - **Input:** **`Radius: 5, Base: 10, Height: 4`**
#    - **Output:**

#    ```markdown
#    Area of Circle: 78.5
#    Area of Triangle: 20
#    ```

radius = int(input("Enter Radius of Circle: "))
base = int(input("Enter Base of a Triangle: "))
height = int(input("Enter Height of a Triangle: "))

area_of_circle = 3.14 * (radius ** 2)
area_of_triangle = 0.5 * base * height

print(f"Area of Circle: {area_of_circle}")
print(f"Area of Triangle: {area_of_triangle}")

print("-" * 63)

#---------------------------------------------------------------------
