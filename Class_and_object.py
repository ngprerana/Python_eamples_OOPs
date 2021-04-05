class Student:
    def __init__(self, name, rollno):
        self.name = name  # Attribute
        self.rollno = rollno  # Attribute

    def talk(self):  # Behaviour
        print("Helooo......!!", self.name)
        print("My roll number is", self.rollno)


s1 = Student("Prerana", 1)  # Object creation
s1.talk()  # calling behaviour of that object = method of object
print("\n")
print("Ouside of class; name:", s1.name)  # directly accessing variables = attributes
print("Ouside of class; roll number:", s1.rollno)  # directly accessing variables = attributes
