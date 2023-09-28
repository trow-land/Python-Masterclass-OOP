class Account:  # reminder: CamelCase (capitalising the first letter of each word)
    """ Simple account class with balance """
# before the init method gets called the __new__ method gets called (which is technically the constructor)
    def __init__(self, name, balance):   # customised the instance
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount

    def show_balance(self):
        print("Balance: ", self.balance)





