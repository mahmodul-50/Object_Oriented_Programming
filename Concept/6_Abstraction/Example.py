from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Bkash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Bkash")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


payments = [Bkash(), Card()]

for p in payments:
    p.pay(500)
