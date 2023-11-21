# Polymorphism has Many Forms --> mainly 4
# 1.Duck Typing (Data Types of variables can change as long as syntax is compatible)  2.Method Overloading 3.Operator Overloading 4.Method Overridding

class Duck:
    def swim(self):
        print("I can swim ")
    def speaks(self):
        print("I can speak")

class Dog:
    def swim(self):
        print("Dog can also swim")
    def speaks(self):
        print("DOg can speak")

def display(duck):
    duck.swim()
    duck.speaks()
    print("In Display function")

d1 = Duck()
display(d1)
d2 = Dog()
display(d2)


# 2. Operator(+, -, *, /) Overloading --> Create Custom Operations for their own values
# But we cannot add imaginary numbers

class ComplexNumbers:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i "

c1 = ComplexNumbers(1, 2)
c2 = ComplexNumbers(4, 5)
print(c1+c2)

# Method Overloading --> By Default Python does not support Method Overloading but can acheive it by other ways
# i> By Provinding some default values we can acheive method overloading
# ii> One Class has many methods with same name but different no. of Parameters
# iii> Using *args(i.e varible length arguments) we can implement Method Overloading in python

class Demo:
    def add(self, a, b, c=0):
        return a+b+c

d = Demo()
print(d.add(3,5))
print(d.add(3, 5, 10))

# OR

class Demo:
    def add(self, *args):
        total = 0
        for i in args:
            total = total+i
        return total

d = Demo()
print(d.add(3,5))
print(d.add(3, 5, 10, 78, 90))


# Method Overriding --> There must be 2 classess , so method overriding is used in / implemented in Inheritance
# Method Name same , Argument Same

class Father:
    def sleep(self):
        print("I sleep early")
    def eat(self):
        print("I eat")
class Son(Father):
    # Derived class has defined this method according to itself
    def sleep(self):
        print("I sleep late")

ram = Son()
ram.sleep()

# Difference Between Method Overloading and Method Overriding
# Method Overloading --> Compile Time Polymorphism (coz at compile time only with help of no. of arguments you pass the appropriate method would be called)
#  Method Overloading --> Occurs between same class
#  Method Overloading --> Same name different parameters
# Method overriding --> Run Time Polymorphism
# Method overriding --> Occur bw 2 classess
# Method overriding --> Same Name, Same Parameters
