# """ 
# Create a class hierarchy:

#     Base class Vehicle with attributes: brand, model, year
#     Derived class Car with additional attribute: number_of_doors
#     Implement a method get_info() in both classes

# """



class Vechicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        print(f"brand: {self.brand}, model: {self.model}, year: {self.year}")

class Car(Vechicle):
    def __init__ (self,brand,model,year,number_of_door):
        super().__init__(brand,model,year)
        self.number_of_door = number_of_door
    def get_info(self):
        super().get_info()
        print(f"number of door: {self.number_of_door}")


car = Car("iphoneCar","SuperAir",2030,4)
car.get_info()


# """
# Write a Python class Rectangle with:

# Private attributes for length and width
# Methods to calculate area (getArea()) and perimeter getPerimeter())
# A method to check if it's a square (isSquare())

# """


class Rectangle:
    def __intit__(self,length,widht):
        self.__length = length
        self.__width = widht
    def getArea(self):
        print(self.__length * self.__width)

    def getPerimeter(self):
        print(2 * (self.__length + self.__width))
    
    def is_square(self):
        print(self.__length == self.__width)

rectangle = Rectangle(5,10)
rectangle.getArea()
rectangle.getPerimeter()
rectangle.is_square()


# """
# Demonstrate polymorphism by creating:

#     A base class Animal with method move()
#     Three derived classes: Fish, Bird, Dog with different implementations of move()
#         fish swims, bird flies, dog runs
#     A function that takes any animal and calls its move() method
# """

class Animal:
    def move(self):
        pass

class Fish(Animal):
    def move(self):
        print("fish swims")

class Bird(Animal):
    def move(self):
        print("bird flys")

class Dog(Animal):
    def move(self):
        print("dog runs")


def animal_move(animal):
    animal.move()

fish = Fish()
bird = Bird()
dog = Dog()
animal_move(fish)
animal_move(bird)
animal_move(dog)
animal_move(dog)
animal_move(fish)