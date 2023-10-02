import datetime
import pytz

class Account:  # reminder: CamelCase (capitalising the first letter of each word)
    """ Simple account class with balance """
    @staticmethod
    def _current_time():  # convention is that names starting with _ are not public
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
        # the self param is not used in the method. Static methods can be used for all instances of the class



# before the init method gets called the __new__ method gets called (which is technically the constructor)
    def __init__(self, name, balance):   # customised the instance
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Unable to withdraw due to insufficient funds")
        self.show_balance()

    def show_balance(self):
        print("Balance: ", self.__balance)

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
                amount *= -1  # shows negative number
            print(amount, transaction_type, "on", date, "|Local time: ", date.astimezone())


if __name__ == '__main__':
    tom = Account("Tom", 0)
    tom.show_balance()

    tom.deposit(1000)
    tom.withdraw(500)
    tom.withdraw(5000)
    tom.show_transactions()

    steph = Account("Steph", 800)
    steph.__balance = 200  # prefixing by __ tells python the mangle the name for us
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40  # This is discouraged hence why it is hard to write
    steph.show_balance()

    # If you end with __ then the name will not get mangled

