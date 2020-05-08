class Account:
    def __init__(self, number, holder, balance, overdraft_limits):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__overdraft_limits = overdraft_limits

    def statement(self):
        print(f'{self.__holder}, you have ${self.__balance} Available')

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value
