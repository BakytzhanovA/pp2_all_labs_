#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
