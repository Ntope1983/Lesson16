# Simple banking system: Person and BankAccount classes with deposit, withdraw, and transfer functionality
class Person:
    def __init__(self, fullname, age, id_number):
        self.fullname = fullname
        self.age = age
        self.id_number = id_number


class BankAccount:
    def __init__(self, person, iban, balance):
        self.person = person
        self.iban = iban
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount}€ to account {self.iban} successful")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount}€ from account {self.iban} successful")
        else:
            print("Insufficient balance")

    def transfer(self, account, amount):
        if self.balance >= amount:
            self.balance -= amount
            account.balance += amount
            print(f"Transfer of {amount}€ from {self.iban} to {account.iban} successful")
        else:
            print("Insufficient balance for transfer")

    def print_balance(self):
        print(f"Account {self.iban} balance: {self.balance}€")


# Create people and accounts
person1 = Person("Daniel Martinez", 23, "47283915")
person2 = Person("Michael Chen", 42, "31859674")

account1 = BankAccount(person1, "FR14 2004 1010 0505 0001 3M02 606", 1000)
account2 = BankAccount(person2, "GB82 WEST 1234 5698 7654 32", 16000)

# Transfer money
account1.transfer(account2, 100)

# Print balances
account1.print_balance()
account2.print_balance()
