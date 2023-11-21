# INHERITENCE

class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I Eat")
    def work(self):
        print("I Work")
class Male(Human):
    def __init__(self, name, num_heart):
        super().__init__(num_heart)
        self.name = name
    def flirt(self):
        print("Hahaha")
    def work(self):
        super().work()
        print("Work in Progress")

male1 = Male("Dipti", 1)
print(male1.num_heart)


# MULTIPLE INHERITANCE
class Human:
    def __init__(self, num_heart):
        print("Calling init from Human")
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I Eat")
    def work(self):
        print("I Work")
class Male:
    def __init__(self, name):
        print("Calling from Male")
        self.name = name
    def flirt(self):
        print("Hahaha")
    def work(self):
        print("Work in Progress")

class Boy(Human, Male):
    def __init__(self, name, heart, language):
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.language = language
    def sleep(self):
        print("Sleep")
    def work(self):
        print("I can test")
    def display(self):
        print(f"Hi I am {self.name} and work on {self.language}")

boy1 = Boy("Rahul",1, "Python")
print(boy1.num_nose)
print(boy1.num_heart)
print(boy1.language)
boy1.display()



