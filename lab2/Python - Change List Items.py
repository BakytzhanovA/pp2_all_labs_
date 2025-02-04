#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)

#Change the second value by replacing it with two new values:

mylist = ["apple", "banana", "cherry"]
mylist[1:2] = ["blackcurrant", "watermelon"]
print(mylist)

#Change the second and third value by replacing it with one value:

fruitlist = ["apple", "banana", "cherry"]
fruitlist[1:3] = ["watermelon"]
print(fruitlist)

#The insert() method inserts an item at the specified index
#Insert "watermelon" as the third item:

fruit_list = ["apple", "banana", "cherry"]
fruit_list.insert(2, "watermelon")
print(fruit_list)