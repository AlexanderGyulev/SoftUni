class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f'Mammals in {self.name_of_zoo}: {", ".join(self.mammals)}\n'
        if species == "fish":
            result += f'Fishes in {self.name_of_zoo}: {", ".join(self.fishes)}\n'
        if species == "bird":
            result += f'Birds in {self.name_of_zoo}: {", ".join(self.birds)}\n'
        result += f"Total animals: {self.__animals}"
        return result


zoo_name = input()
obj = Zoo(zoo_name)

total_entries = int(input())

for items in range(total_entries):
    animal_species, animal_name = input().split(" ")
    obj.add_animal(species=animal_species, name=animal_name)

species_type = input()
print(obj.get_info(species_type))
