# Polymorphism example
class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Paddle, paddle, paddle")

    def quack(self):
        print("Quack, quack, quack")

class Penguin(object):

    def walk(self):
        print("Waddle, waddle, waddle I waddle too")

    def swim(self):
        print("Paddle, paddle, paddle, the water is warmer here")

    def quack(self):
        print("I'm a penguin mate")

def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)  # as far as the function is concerned percy is a duck
