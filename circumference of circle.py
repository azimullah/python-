import math
r=float(input("Enter the radius of the circle: "))
pi = math.pi
# This code calculates the circumference of a circle given its radius.
# The formula for the circumference is C = 2 * π * r, where r is the radius and π (pi) is approximately 3.14159.
def find_circumference(radius):    
    return 2 * pi * radius

circumference= find_circumference(r)
print(f"The circumference of the circle with radius {r} is: {circumference}")

