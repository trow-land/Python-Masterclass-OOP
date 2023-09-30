# Each class will be in its own file for the sake of this exercise

from enemy import Enemy, Troll

ugly_troll = Troll()
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug", 18, 1)
print("Another troll - {}".format(another_troll))

brother = Troll("Urg", 23)
print("Brother - {}".format(brother))




