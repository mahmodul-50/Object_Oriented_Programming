class GrandParent:
    def house(self):
        print("Grandparent's house")


class Parent(GrandParent):
    def car(self):
        print("Parent's car")


class Child(Parent):
    def bike(self):
        print("Child's bike")


c = Child()
c.house()
c.car()
c.bike()

# Concept
# Chain inheritance (A → B → C)
