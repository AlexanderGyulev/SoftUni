class Party():
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def total_names(self):
        return f'{", ".join(party.people)}'

    def number_of_people(self):
        return f'{len(party.people)}'


party = Party()
names = input()
while names != "End":
    party.invite(names)
    names = input()

print(f'Going: {party.total_names()}')
print(f'Total: {party.number_of_people()}')
