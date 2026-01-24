class BankAccount:
    def __init__(self, iban, fullname, amount):
        self.iban = iban
        self.fullname = fullname
        self.amount = amount

    def deposit(self, account, amount):
        if self.amount >= amount:
            self.amount -= amount
            account.amount += amount
            print(
                f"Η κατάθεση {amount} € από το λογαριασμό {self.iban} στον λογαριασμό {account.iban} πραγματοποιηθείτε με επιτυχία ")
        else:
            print("Ανεπαρκές Υπόλοιπο Λογαριασμού")

    def print_amount(self):
        print(f"To Υπόλοιπο λογαριασμού είναι: {self.amount}")


class Person:
    def __int__(self, fullname, age, id_number):
        self.fullname = fullname
        self.age = age
        self.id_number = id_number


account1 = BankAccount("GB82 WEST 1234 5698 7654 32", "John Polydoras", 1000)
account2 = BankAccount("GR82 WEST 1234 5698 7654 33", "Sot Papadopoulos", 16000)
account1.deposit(account2, 100)
account1.print_amount()
account2.print_amount()
person1 = Person("name", 23, "name")
