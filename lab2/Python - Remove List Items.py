#The remove() method removes the specified item
#Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]
this_list.remove("banana")
print(this_list)

#The pop() method removes the specified index.
#Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
#Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
#Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
#Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

#The clear() method empties the list.
#The list still remains, but it has no content.

#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)