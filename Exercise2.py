class Philosopher:
    def __init__(self, fullname, era, books, school):
        self.fullname = fullname
        self.era = era
        self.books = books
        self.school = school
        self.disputed_works = []


plato = Philosopher("Plato", "Ancient Greece", ["The Republic", "Phaedon"], "Platonism")
spinoza = Philosopher("Baruch Spinoza", "Modern Netherland", ["Ethics", "Political Treatise"], "Rationalism")
print(plato.disputed_works)
print(spinoza.disputed_works)
