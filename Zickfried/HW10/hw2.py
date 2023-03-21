class Human():
    
    def __init__(self, name = "Peter"):
        self.name = name
    
    def getGreeting(self):
        return f"Wellcome {self.name}!" 
    
    def getSpecies(self):
        self.species = "Homosapiens"
        return self.species
    
    @staticmethod
    def static_messege(): 
        return "Nice to meet you!"
    
# human_1 = Human("Grisha")

# print(human_1.static_messege())    
      