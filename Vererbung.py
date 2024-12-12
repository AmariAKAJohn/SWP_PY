class Hund():
    def __init__(self, name):
        self.name = name
    
    def bellen(self):
        print("Wuff!")
    
    def fressen(self):
        print("Hund frisst")

    def __str__(self):
        return self.name + " ist ein Hund"
    
class Katze(Hund):
    def __init__(self, name):
        super().__init__(name)
    
    def bellen(self):
        print("Miau!")
    
    def fressen(self):
        print("Katze frisst")

    def __str__(self):
        return self.name + " ist eine Katze"
    
a = Katze("Minka")
print(a)
#-----------------------------------------
#Danda: Verbindung Buildin mit Fixen Code 