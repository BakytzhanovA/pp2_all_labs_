# Lists are used to store multiple items in a single variable
# Example
#Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List items are indexed, the first item has index [0], the second item has index [1] etc

# Since lists are indexed, lists can have items with the same value:
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)

# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

# Using the list() constructor to make a List:

mylist = list(("apple", "banana", "cherry")) 
print(mylist)