if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello, World!"

# Python Comments

#this is a comment
print("Hello, World!")
print("Hello, World!")  #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

# This is a comment
# Written in
# More than just one line
print("Hello, World!")

"""
This is a comment 
written in 
more than just one line
"""
print("Hello, World!")

# Python Variables

x = 5
y = "John"
print(x)
print(y)

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

# Get the Type
x = 5
y = "John"
z = 3.0
print(type(x))
print(type(y))
print(type(z))

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a

# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#  Output Vriables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print( x, y, z)

x = "Python "
y = "is "
z = "awesome"
print( x + y + z)

x = 5
y = 10
print(x + y)

# Global Variables

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# The global keyword

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)