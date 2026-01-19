class Philosopher:
    def __init__(self, fullname, era, books, school):
        self.fullname = fullname
        self.era = era
        self.books = books
        self.school = school
        self.questionable_works = []


plato = Philosopher("Plato", "Ancient Greece", ["The Republic", "Phaedon"], "Platonism")
spinoza = Philosopher("Baruch Spinoza", "Modern Netherland", ["Ethics", "Political Treatise"], "Rationalism")
print(plato.questionable_works)
print(spinoza.questionable_works)
