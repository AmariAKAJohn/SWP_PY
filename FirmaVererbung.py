class Firma():

    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def get_all_mitarbeiter(self):
        allMitarbeiter = 0
        for abteilung in self.abteilungen:
            allMitarbeiter += len(abteilung.mitarbeiter)
        return allMitarbeiter
    
    def get_all_abteilungsleiter(self):
        allAbteilungsleiter = 0
        for abteilung in self.abteilungen:
            allAbteilungsleiter += 1
        return allAbteilungsleiter
    
    def get_all_abteilungen(self):
        return self.abteilungen.count()
    
    def get_biggest_abteilung(self):
        biggestAbteilung = None
        maxMitarbeiter = 0
        for abteilung in self.abteilungen:
            if len(abteilung.mitarbeiter) > maxMitarbeiter:
                maxMitarbeiter = len(abteilung.mitarbeiter)
                biggestAbteilung = abteilung
        return biggestAbteilung

    def prozent_männer_frauen(self):
        allMitarbeiter = self.get_all_mitarbeiter()
        anzahlMänner = 0
        anzahlFrauen = 0
        for mitarbeiter in allMitarbeiter:
            if mitarbeiter.geschlecht == "m":
                anzahlMänner += 1
            else:
                anzahlFrauen += 1
        print("Männer: " + str(anzahlMänner / len(allMitarbeiter) * 100))
        print("Frauen: " + str(anzahlFrauen / len(allMitarbeiter) * 100))
        #print("Männer = " + str((len(allMitarbeiter) / anzahlMänner) * 100))
        #print("Frauen = " + str((len(allMitarbeiter) / anzahlFrauen) * 100)) 

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

johannes = Mitarbeiter("Johannes", "m", 3000)
john = Mitarbeiter("John", "m", 3000)
jane = Mitarbeiter("Jane", "w", 4000)
peter = Mitarbeiter("Peter", "m", 3500)
hans = Mitarbeiter("Hans", "m", 3200)
gabe = Mitarbeiter("Gabe", "m", 3100)

edv = Abteilung("EDV", john)
info = Abteilung("Info", jane)

edv.add_mitarbeiter(jane)
edv.add_mitarbeiter(peter)
edv.add_mitarbeiter(johannes)

info.add_mitarbeiter(hans)
info.add_mitarbeiter(gabe)

firma = Firma("John AG")
firma.add_abteilung(edv)
firma.add_abteilung(info)

print(firma.get_biggest_abteilung())