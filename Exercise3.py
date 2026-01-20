class Dog():
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.mood = 5

    def eat(self):
        self.mood += 1

    def bark(self):
        if self.mood > 5:
            print("Woof WoofWoof")
        else:
            print("Woof")

    def walk(self):
        self.mood += 1


pico = Dog("Pico", 20, "Terrier")
pico.bark()
pico.walk()
pico.bark()
pico.walk()
pico.bark()
pico.eat()
pico.bark()
