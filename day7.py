# Polymorphism
# method overiding

# class Shape:
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()

#     def area(self):
#         return 3.14*self.radius**2
    
#     def print_area(shape):
#         print ("Area:",shape.area)

# circle = Circle(4)
# print_area(circle)



class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Wooof !"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_sound(animal):
        print(animal.speak())
    

animal = [Dog(), Cat()]