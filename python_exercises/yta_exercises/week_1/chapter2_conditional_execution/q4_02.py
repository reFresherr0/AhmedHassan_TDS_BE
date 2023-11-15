# Take input from user
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

# Check for equilateral triangle
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
# Check for isosceles triangle
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is an isosceles triangle.")
# Check for scalene triangle
else:
    print("The triangle is a scalene triangle.")
