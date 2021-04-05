class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def talk(self):
        print("Helooo......!!", self.name)
        print("My roll number is", self.rollno)


s1 = Student("Prerana", 1)

s2 = Student("Harsh", 2)

# Call talk() method
Student.talk(s1)  # called method using class; here we are passing s1 as parameter for self
print()
s2.talk()  # called method using object; python machine implicitly assigns s2 for self   # recommended
print()
print("s1:", id(s1))
print("s2:", id(s2))
