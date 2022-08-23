class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far:', self.x)

#puts the class name to a variable to make it easier to program
an = PartyAnimal()
an.party()
an.party()
an.party()

#print(ord('H)) --> tells us the numeric value of a simple ASCII character
