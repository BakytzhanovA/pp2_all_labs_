#Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
#Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#By leaving out the start value, the range will start at the first item:
#This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])