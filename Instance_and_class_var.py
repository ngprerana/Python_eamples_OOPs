class Student:
    college_name = "SSIT"                           # class variable

    def __init__(self, name, rollno):
        self.name = name                            # instance variable
        self.rollno = rollno                        # instance variable


s1 = Student("Prerana", 1)

print("using class var: ", Student.college_name)    # recommended to use class name to fetch class variables
print("using ref var: ", s1.college_name)           # class variable through reference variable
print("name:", s1.name)
print("roll number:", s1.rollno)
