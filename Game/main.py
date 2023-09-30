# Each class will be in its own file for the sake of this exercise

from player import Player

tom = Player("Tom")

print(tom.name)
print(tom.lives)
tom.lives -= 1
print(tom)

tom.lives -= 1
print(tom)

tom.lives -= 1
print(tom)

tom.lives -= 1
print(tom)

tom.level += 1
print(tom)

tom.level += 1
print(tom)

tom.level += 1
print(tom)

tom.level += 5
print(tom)

tom.level -= 3
print(tom)

