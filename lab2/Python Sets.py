#Sets are used to store multiple items in a single variable.

#A set is a collection which is unordered, unchangeable*, and unindexed.

#Set items are unchangeable, but you can remove items and add new items.

#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))