class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # underscore hides it
        self._level = 1
        self._score = 0


    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can not be negative")
            self._lives = 0



    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            old_level = self._level  # old level value
            self._level = level  # new level value
            self._score += 1000 * (level - old_level)
        else:
            print("The level can not go below 1")
            self._level = 1



    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
























