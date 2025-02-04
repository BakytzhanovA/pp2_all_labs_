# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Return the third, fourth, and fifth item:

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[:4])

#This example returns the items from "cherry" to the end:

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[-4:-1])

#Check if "apple" is present in the list:

fruit_list = ["apple", "banana", "cherry"]
if "apple" in fruit_list:
  print("Yes, 'apple' is in the fruits list")