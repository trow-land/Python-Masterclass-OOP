# Each class will be in its own file for the sake of this exercise

from enemy import Enemy, Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print("Brother - {}".format(brother))

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()


vampire = Vampyre("Dracula")
print(vampire)
vampire.hit_points -= 3
vampire.take_damage(5)
print(vampire)


print("-" * 40)
another_troll.take_damage(30)
print(another_troll)


