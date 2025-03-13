import enum
import sys

class RoomType(enum.Enum):
    Einzelzimmer = 1
    Doppelzimmer = 2

class Room:
    def __init__(self, nr, typ, preis, verfügbar):
        self.nr = nr
        self.typ = typ
        self.preis = preis
        self.verfügbar = verfügbar
    
    def __str__(self):
        return f'Zimmer Nummer: {self.nr}, Typ: {self.typ}, Preis: {self.preis}, Verfügbar: {"Nein" if not self.verfügbar else "Ja"}'

class Hotel:
    zimmer = []
    def book_room_random(self):
        inputtype = input("Welches Zimmer möchten Sie buchen? (Einzelzimmer (1) oder Doppelzimmer (2)): ")
        room_type = None 
        try:
            inputtype = int(inputtype)
            room_type = RoomType(inputtype)  
        except KeyError:
            print("Bitte geben Sie eine gültige Nummer ein")
        except ValueError:
            print("Bitte geben Sie 1 oder 2 ein")

        for z in self.zimmer:
            if z.verfügbar == True and z.typ == room_type:
                z.verfügbar = False
                return z
                
        return "Zimmer nicht verfügbar" 
            
    def book_with_numnber(self, nr):
        for z in self.zimmer:
            if z.nr == nr and z.verfügbar == True:
                z.verfügbar = False
                return z
        return "Zimmer nicht verfügbar"
    
    def cancle_booking(self, nr):
        for z in self.zimmer:
            if z.nr == nr and z.verfügbar == False:
                z.verfügbar = True
                return z
        return "Zimmer nicht gebucht"
    
    def anzahlFreieZimmer(self):
        anzahlZimmer = 0
        for zim in self.zimmer:
            if zim.verfügbar == True:
                anzahlZimmer += 1
        return anzahlZimmer
def main():
    hotel = Hotel()
    hotel.zimmer.append(Room(1, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(2, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(3, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(4, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(5, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(6, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(7, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(8, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(9, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(10, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(11, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(12, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(13, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(14, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(15, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(16, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(17, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(18, RoomType.Doppelzimmer, 100, True))
    hotel.zimmer.append(Room(19, RoomType.Einzelzimmer, 50, True))
    hotel.zimmer.append(Room(20, RoomType.Doppelzimmer, 100, True))

    print(hotel.book_room_random())
    print(hotel.book_with_numnber(3))

    print(hotel.anzahlFreieZimmer())
    
    print(hotel.cancle_booking(3))

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print("Ein Fehler ist aufgetreten: ", err)
        sys.exit(1)