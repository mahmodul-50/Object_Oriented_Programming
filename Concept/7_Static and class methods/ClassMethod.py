# Concept
# Uses cls
# Works with class variables
# Affects all objects

class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    def display(self):
        print(f"Name: {self.name}")
        print(f"School: {Student.school_name}")


s1 = Student("Rahim")
s2 = Student("Karim")

Student.change_school("XYZ School")

s1.display()
print()
s2.display()
