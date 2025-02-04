# In programming you often need to know if an expression is True or False
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
#example :
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:
#example :

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))

#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())

#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
#Check if an object is an integer or not:

x = 200
print(isinstance(x, int))