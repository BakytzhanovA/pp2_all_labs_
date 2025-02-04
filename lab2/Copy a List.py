#You can use the built-in List method copy() to copy a list.
#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#You can also make a copy of a list by using the : (slice) operator.
#Make a copy of a list with the : operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)