class Firma():

    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def __str__(self):
        allAbteilungen = ""
        for abteilung in self.abteilungen:
            allAbteilungen += abteilung.__str__() + ", "
        return allAbteilungen
        

class Person():
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht

class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, gehalt):
        super().__init__(name, geschlecht)
        self.gehalt = gehalt

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, gehalt):
        super().__init__(name, geschlecht, gehalt)


class Abteilung():
    def __init__(self, name, leiter):
        self.name = name
        self.mitarbeiter = []
        self.leiter = leiter

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def add_leiter(self, leiter):
        self.leiter = leiter

    def __str__(self):
        return "Abteilung " + self.name + " hat: " +  str(len(self.mitarbeiter)) + " Mitarbeiter" + " und wird geleitet von: " + self.leiter.name

john = Mitarbeiter("John", "m", 3000)
jane = Mitarbeiter("Jane", "w", 4000)
peter = Mitarbeiter("Peter", "m", 3500)
hans = Mitarbeiter("Hans", "m", 3200)
gabe = Mitarbeiter("Gabe", "m", 3100)

edv = Abteilung("EDV", john)
info = Abteilung("Info", jane)

edv.add_mitarbeiter(jane)
edv.add_mitarbeiter(peter)

info.add_mitarbeiter(hans)
info.add_mitarbeiter(gabe)

firma = Firma("John AG")
firma.add_abteilung(edv)
firma.add_abteilung(info)

print(firma)