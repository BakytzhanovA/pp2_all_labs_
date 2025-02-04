#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
#Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
#Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#You can use the range() function to create an iterable:

thislist = [x for x in range(10)]