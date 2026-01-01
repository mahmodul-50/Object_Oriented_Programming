class Account:
    def __init__(self, balance):
        self._balance = balance  # protected

    def show_balance(self):
        print("Balance:", self._balance)


class SavingsAccount(Account):
    def deposit(self, amount):
        self._balance += amount


acc = Account(1000)
acc.deposit(500)
acc.show_balance()

# still accessible
print(acc._balance)
