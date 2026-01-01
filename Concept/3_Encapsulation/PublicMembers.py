class Student:
    def __init__(self, name, marks):
        self.name = name  # public
        self.marks = marks  # public

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


s = Student("Rahim", 85)

# direct access (allowed)
s.display()
s.marks = 90
print("Updated Marks:", s.marks)
