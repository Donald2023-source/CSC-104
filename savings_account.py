from account import Account


class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self,balance)