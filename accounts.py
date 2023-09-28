import datetime
import pytz

class Account:  # reminder: CamelCase (capitalising the first letter of each word)
    """ Simple account class with balance """
# before the init method gets called the __new__ method gets called (which is technically the constructor)
    def __init__(self, name, balance):   # customised the instance
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Unable to withdraw due to insufficient funds")
        self.show_balance()

    def show_balance(self):
        print("Balance: ", self.balance)

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
                amount *= -1  # shows negative number
            print(amount, transaction_type, "on", date, date.astimezone())


if __name__ == '__main__':
    tom = Account("Tom", 0)
    tom.show_balance()

    tom.deposit(1000)
    tom.withdraw(5000)

# we want to be able to log the transaction details



