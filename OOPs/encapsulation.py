# Provides Security
# Can also be said Data Hiding/ Actual hiding is done using encapsulation using access modifiers
# Using getters and setters methods we can acheive Encapsulation
# Using getters and setters we can access private kind of thing
# getter method is used to access private data
# setter method is used to set/modify the values
# no need to write getter and setter just indicating is enough
# We use getter and setter method when we want to avoid direct access to private data


class Student:
    def __init__(self, name, roll_number, age):
        # This is a Public variable
        self.name = name
        # Just putting single underscore before the variable means this is PROTECTED Variable
        self._roll_number = roll_number
        # this variable age is a Private variable
        self.__age = age

    # This is a getter function 
    def get_age(self):
        return self.__age
    
    # This is a setter function
    def set_age(self, age):
        if age > 35:
            print("Invalid Age")
        else:
            self.__age = age
            print(f"The Age of User is {age}")

s1 = Student("Dipti", 23, 20)
print(s1.get_age())
s1.set_age(34)




