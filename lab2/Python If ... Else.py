#Example
#If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#The else keyword catches anything which isn't caught by the preceding conditions.
#example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#You can also have an else without the elif:
#Example

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")