#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

#Strings are Arrays
c = "Hello, World!"
print(c[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
d = "Hello, World!"
print(len(d))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)