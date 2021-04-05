class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap1 = self.Laptop()                           # object of inner class is created

    def talk(self):
        print("Helooo......!!", self.name)
        print("My roll number is", self.rollno)
        self.lap1.show_config()                             # accessing inner class

    class Laptop:  # Inner class
        def __init__(self):
            self.brand = "hp"
            self.ram = "8gb"

        def show_config(self):
            print("Inside Inner Class")
            print("Brand:", self.brand)
            print("RAM:", self.ram)


s1 = Student("Prerana", 1)
s1.talk()
print("Object of inner class created from outside")
lap2 = Student.Laptop()                                     # object of inner class is created
lap2.show_config()
