# class Instructor:
#     pass
# instructor_1 = Instructor()
# inst_2 = Instructor()
# print(type(instructor_1))
# print(type(inst_2))

class Instructor:
    def __init__(self, ins_name, ins_add):
        self.name = ins_name
        self.address = ins_add

inst_1 = Instructor("Dipti", "Address1")
print(inst_1)
print(inst_1.name)
print(inst_1.address)