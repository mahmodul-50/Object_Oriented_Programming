class Laptop:
    # default constructor
    def __init__(self):
        self.brand = "Lenovo"
        self.price = 130000

    # instance method
    def show_details(self):
        print(f"Brand: {self.brand}\nPrice: {self.price}")


l1 = Laptop()
l1.show_details()
