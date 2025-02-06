## Name: Cory Strong
## Class: CSCI 101
## File Name : ShapeCalc_CStrong.py
## Discription : This program prompts users to input a shape which allows them to calculate formulas for each shape
print("Shapes Available:")
shape_Circle = ("Circle")
shape_Cylinder = ("Cylinder")
shape_Rectangle = ("Rectangle")
width = 13
print(shape_Circle.center(width))
width = 16
print(shape_Cylinder.center(width))
width = 17
print(shape_Rectangle.center(width))

import math
shape_selected = input("Which shape would you like to use?").lower()
if shape_selected == "circle":
    print()
    radius = float(input("Enter the radius of the circle:"))
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    print(f"    {'Area of Circle is:'} {area:.2f}")
    print(f"    {'Circumference of Circle is:'} {circumference:.2f}")
#Cylinder calculation
elif shape_selected == "cylinder":
    print()
    height = float(input("Enter the height of the cylinder:"))
    radius = float(input("Enter the radius of the cylinder:"))
    volume = math.pi * (radius ** 2) * height
    surface_area = 2 * math.pi * radius * (radius + height)
    print(f"    {'Volume of Cylinder is:'} {volume:.2f}")
    print(f"    {'Surface Area of Cylinder is:'} {surface_area:.2f}")
#rectangle calculation
elif shape_selected == "rectangle":
    print()
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"    {'Area of Rectangle is:'} {area:.2f}")
    print(f"    {'Perimeter of Rectangle is:'} {perimeter:.2f}")
else:
    print(shape_selected ,"is not a valid available shape...")
