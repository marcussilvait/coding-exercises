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

    def __allowed_to_withdraw(self, requested_value):
        value_available = self.__balance + self.__overdraft_limit
        return value_available >= requested_value

    def withdraw(self, value):
        if self.__allowed_to_withdraw(value):
            self.__balance -= value
        else:
            print(f'Requested value ${value} above the available limit')

    def transfer(self, valor, allocation):
        self.withdraw(valor)
        allocation.deposit(valor)

    @property
    def number(self):
        return self.__number.title()

    @property
    def holder(self):
        return self.__holder

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, overdraft_limit):
        self.__overdraft_limit = overdraft_limit

    @staticmethod
    def bank_cod():
        return '001'

    @staticmethod
    def banks_cods():
        return {'BB': '001', 'Nubank': '260', 'Inter': '770'}


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
