class Account:
    def __init__(self, number, holder, balance, overdraft_limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__overdraft_limit = overdraft_limit

    def statement(self):
        print(f'{self.__holder}, you have ${self.__balance} Available')

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def transfer(self, valor, allocation):
        self.withdraw(valor)
        allocation.deposit(valor)

    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, overdraft_limit):
        self.__overdraft_limit = overdraft_limit


class Client:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('calling @property name()')
        return self.__name.title()

    @name.setter
    def name(self, name):
        print('calling setter name()')
        self.__name = name
