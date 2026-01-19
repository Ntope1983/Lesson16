class Dog():
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed


pico=Dog("Pico", 20, "Terrier")
lassie=Dog("Lassie",15,"Coley")

print(pico.breed)
print(lassie.breed)