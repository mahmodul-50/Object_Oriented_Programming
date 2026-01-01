class Person:
    # parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    # method
    def can_vote(self):
        return self.age >= 18


p1 = Person("Rahim", 22)
p2 = Person("Karim", 16)

p1.display()
print("Can vote:", p1.can_vote())

print()

p2.display()
print("Can vote:", p2.can_vote())
