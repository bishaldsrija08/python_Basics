# Basic type of class
class A:
    def display_name():
        print("This is class A.")

class B(A):
    def print_name():
        print("This is class B.")
# A.display_name()

obj = A()
obj.display_name()  # This will raise a TypeError because 'self' is missing.# To fix the error, we need to add 'self' as the first parameter of the method

