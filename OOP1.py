class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):  # methods contain the self parameter
        self.on = True

kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)  # 8.99

kenwood.price = 12.75
print(kenwood.price)  # 12.75

hamilton = Kettle("Hamilton", 14.75)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models:", kenwood.make, "=", kenwood.price, ",", hamilton.make, "=", hamilton.price)

print(hamilton.on)  # False
hamilton.switch_on()  # Using the instance
print(hamilton.on)  # True

Kettle.switch_on(kenwood)  # Using the class itself instead of the instance
print(kenwood.on)  # True

print("*" * 80)
kenwood.power = 1.5  # Adds another data attribute to the kenwood object
print(kenwood.power)

# print(hamilton.power)  # AttributeError: 'Kettle' object has no attribute 'power'










