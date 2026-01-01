class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(2000)
acc.deposit(500)

print("Balance:", acc.get_balance())

# will cause error
# print(acc.__balance)
