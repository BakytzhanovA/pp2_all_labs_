#A tuple is a collection which is ordered and unchangeable.
#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Since tuples are indexed, they can have items with the same value:
#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function:
#Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Tuple items can be of any data type:
#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")