class Dog:
    "This class represents an animal known as a dog"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
        self.species = "Canis familiaris"
        
    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name + " knows " + trick)

    def knows(self, trick):
        if trick in self.tricks:
            print("Yes " + self.name + " knows " + trick)
            return True
        else:
            print("No " + self.name + " doesn't know " + trick)
            return False

