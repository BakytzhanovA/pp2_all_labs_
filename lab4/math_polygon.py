import math
num_of_sides = float(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
area = (num_of_sides * length ** 2) / 4 * math.tan(math.pi/num_of_sides)
new_area = math.ceil(area)

print("The area of the polygon is:",new_area)