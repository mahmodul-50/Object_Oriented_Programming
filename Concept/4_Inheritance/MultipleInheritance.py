class Father:
    def skill(self):
        print("Father: Driving")


class Mother:
    def skill(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def own_skill(self):
        print("Programming")


c = Child()
c.skill()        # Method Resolution Order (MRO)
c.own_skill()

print(Child.__mro__)
