class Account:
    def __init__(self, number, holder, balance, overdraft_limits):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.overdraft_limits = overdraft_limits

    def statement(self):
        print(f'{self.holder}, you have ${self.balance} Available')

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value
