class Program:
    def __init__(self, name, year):
        self._name = name
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, likes):
        self._likes = likes


class Movie(Program):
    actor = 'Selton Melo'

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    @classmethod
    def info(cls):
        return f'This s a classmethod with the brazilian actor {cls.actor}'

    @staticmethod
    def log():
        return f'This is a staticmethod log'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons
