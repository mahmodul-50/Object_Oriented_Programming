class Employee:
    # class attribute (shared)
    company_name = "ABC"

    def __init__(self, name, salary):
        # instance attributes (unique)
        self.name = name
        self.salary = salary

    # instance method
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.company_name}")

    # instance method to update salary
    def increment_salary(self, amount):
        self.salary += amount


e1 = Employee("Mahmodul", 30000)
e2 = Employee("Hasan", 25000)

print("# before modifying")
e1.show_details()
print()
e2.show_details()
e1.increment_salary(5000)

# modify class attribute
Employee.company_name = "XYZ"

print("# before modifying")
e1.show_details()
print()
e2.show_details()