# Print Hello World in python
print("Hello World!")

# indentation maatters
if 5>4:
    print("Greatest!")

# Type casting in python

# Implicit type casting
aaaa=4
bbb=5.5
ccc=aaaa  + bbb
print(ccc)


# Explicit type casting

a= '7.7'
b=6
c=float(a) + b
print(c)

# Input/Output statement in Python

name = input("Enter your name: ")
print(f"My name is {name}.")


# String formatting in python

f_name = "Bishal"
print(f"{f_name}")
print("{}".format(f_name))

# Simple calculator

num1 = int(input("Enter first number: "))
num2= int(input("Enter second number: "))

print("Sum is", num1+num2)