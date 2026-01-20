#Modeling in OOP 
class Flat:
    def __init__(self):
        self.people = 0

    def add_people(self, people):
        self.people += people


class Storey:
    def __init__(self, number_flats):
        self.flats = [Flat() for _ in range(number_flats)]
        self.people = 0


class Building:
    def __init__(self, number_storeys, number_flats):
        self.storeys = [Storey(number_flats) for _ in range(number_storeys)]


building_a = Building(3, 5)
building_a.storeys[0].flats[2].add_people(4)

for st in building_a.storeys:
    for fl in st.flats:
        print(fl.people)
