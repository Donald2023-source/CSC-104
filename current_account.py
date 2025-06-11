from account import Account

class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def withdraw(self, amount, limit):
        if amount < limit:
            super().withdraw(amount)