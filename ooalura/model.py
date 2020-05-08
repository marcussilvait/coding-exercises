class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    def __str__(self):
        return f'{self.name}. {self.year}. {self._likes} likes'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def likes(self):
        return self._likes

    def like_up(self):
        self._likes += 1


class Movie(Program):
    actor = 'Selton Melo'

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self.name}. {self.year}. {self.duration} min. {self._likes} likes'

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

    def __str__(self):
        return f'{self.name}. {self.year}. {self.seasons} seasons. {self._likes} likes'


avangers = Movie('avangers endgame', 2019, 160)
friends = Series('frieds', 1994, 10)

# Adding likes to programs
avangers.like_up()
for i in range(1, 6):
    friends.like_up()

my_playlist = [avangers, friends]

for program in my_playlist:
    print(program)
