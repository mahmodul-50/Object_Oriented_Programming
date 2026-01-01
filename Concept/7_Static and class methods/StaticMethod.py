    
# Concept
#     Does not use self
#     Does not depend on object
#     Works like a normal function inside a class
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0


print(MathUtils.add(10, 5))
print(MathUtils.is_even(8))
