from account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        if amount < 6000:
            super().withdraw(amount)
        else:
            print("Withdrawal amount exceeds the limit of N6000 for Current Account.")
    def deposit(self, amount):
        return super().deposit(amount)