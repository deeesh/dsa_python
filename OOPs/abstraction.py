from abc import ABC, abstractmethod
# This Vehicle function written in differnt file so that some things hidden from user
# @ symbol for abstract class if we will not add this decorator than this class will not become abstract class
# We cannot create object of abstract class

class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_types = n
    @abstractmethod
    def start(self):
        pass
    def display(self):
        print("Absract Class Working")

class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color=color
    def start(self):
        print("Start with Kick")

class Scooty(Vehicle):
    def __init__(self, n):
        super().__init__(n)
    def start(self):
        print("Self Start")

class Car(Vehicle):
    def __init__(self, n, x):
        super().__init__(n)
        self.no_of_gear = 6
    def start(self):
        print("Start using key")

bike = Bike(2, "Black")
bike.start()
bike.display()
    


    