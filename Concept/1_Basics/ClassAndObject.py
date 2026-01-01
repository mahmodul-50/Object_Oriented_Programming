class Student:
    institute = "CUET"  # class attribute
    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display_info(self):
        print(f"Name: {self.name}\nID: {self.id}\nInstitute: {self.institute}\n")
        
s1 = Student("Mahmodul", 2001) # this are objects
s2 = Student("Hasan", 2000)

s1.display_info()
s2.display_info()

print(type(s1))
