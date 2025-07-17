# class
class Calculation:
    def add(self, a,b):
        return a+b
calculator = Calculation()
result = calculator.add(4,5)
print(result)

# Inheritance
class Animal:
    def __init__(self, name):
        print("Animal constructor is called", name)
        self.__name = name

    def eat(self):
        print("I can eat.")

    def sleep(self):
        print("I can sleep.")
    
class Dog(Animal):
    def bark(self):
        print(self.name)
        print("Dog can bark.")

dog1= Dog('Gernam Sheperd')
result1 = dog1.bark()
print(dog1.name)
# print(result1)