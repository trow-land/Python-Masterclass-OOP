'''
Class: template for creating object. All objects created using the same class will have the same characteristics.
Object: an instance of a class
Instantiate: create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
Dunder: __ (the double underscore means do not change!
'''


class Kettle(object):

    # class attributes  (similar to static in c++)
    power_source = "electricity"

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

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)  # atomic
kenwood.power_source = "gas"
print(kenwood.power_source)  # gas
print(hamilton.power_source)  # atomic
print(Kettle.__dict__)  # {'__module__': '__main__', 'power_source': 'electricity', '__init__': <function Kettle.__init__ at 0x0000020746BEA200>, 'switch_on': <function Kettle.switch_on at 0x0000020746BE8F40>, '__dict__': <attribute '__dict__' of 'Kettle' objects>, '__weakref__': <attribute '__weakref__' of 'Kettle' objects>, '__doc__': None}
print(kenwood.__dict__)  # {'make': 'kenwood', 'price': 12.75, 'on': True, 'power': 1.5}
print(hamilton.__dict__)  # {'make': 'Hamilton', 'price': 14.75, 'on': True}









