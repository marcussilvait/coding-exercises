from abc import ABCMeta, abstractmethod


class Program(metaclass=ABCMeta):
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @abstractmethod
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


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

    @property
    def programs(self):
        return self._programs

    @property
    def length(self):
        return len(self._programs)


avengers = Movie('avengers endgame', 2019, 160)
wick = Movie('john wick parabellum', 2019, 180)
friends = Series('friends', 1994, 10)
office = Series('the office', 2004, 9)

# Adding likes to programs
avengers.like_up()
wick.like_up()
for i in range(1, 6):
    friends.like_up()
    office.like_up()

my_programs = [avengers, wick, friends, office]
my_playlist = Playlist('weekend', my_programs)

print(f'Playlist length: {len(my_playlist)}')

for program in my_playlist:
    print(program)
