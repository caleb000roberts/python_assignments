class Pet:
    def __init__(self, petType, name, age, weight, color, isVaccinated, isSpayedOrNeutered, note) :
        self.petType = petType
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.isVaccinated = isVaccinated
        self.isSpayedOrNeutered = isSpayedOrNeutered
        self.note = note



class Dog(Pet):
    def __init__(self, petType, name, age, weight, color, isVaccinated, isSpayedOrNeutered, note, heartwormCheck) :
        super().__init__( petType, name, age, weight, color, isVaccinated, isSpayedOrNeutered, note)
        self.heartwormCheck = heartwormCheck

def __repr__(self):
        return(f"Pet Type: {self.petType}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Color: {self.color}, Vaccinated: {self.isVaccinated}, Spayed/Neutured: {self.isSpayedOrNeutered}, Heartworms: {self.heartwormCheck}, Notes: {self.note}")

class Cat(Pet):
    def __init__(self, felineLeukimiaCheck):
        super().__init__()
        self.felineLeukimiaCheck = felineLeukimiaCheck






spike = Dog("Dog","Spike", 4, "24 lbs", "brown", True, True, "Sometimes aggressive", True)
#meeko = Dog("Meeko", 2, "76 lbs", "white w/ spots", True, False,  "Needs shots updated", False)
#lacey = Dog("Lacey", 12, "29 lbs", "brindle", False, False, "Great health for age", False)

#sylvester = Cat("Sylvester", 1, "9 lbs", "black and white", True, True, "Flea medication reccommended", False)
#taco = Cat("Taco", 14, "11 lbs", "orange", True, True, "Check for pregnancy", False)
#skippy = Cat("Skippy", 3, "4 lbs", "white and brown", True, False, "Treatment started bi-weekly", True)


print(spike)


    
    