import sys
class Auto:
    def __init__(self, ps):
        self.ps = ps
    
    def __add__(self, other):
        try:
            add = self.ps + other.ps           
        except AttributeError:
            return "Keine Addition möglich"
        return add

    def __sub__(self, other):
        if not isinstance(other, Auto):
            return "Autos müssen mit anderen Autos subtrahiert werden"

        if(self.ps - other.ps < 0):
            raise ValueError("Negative PS nicht möglich")

        return self.ps - other.ps
    
    def __truediv__(self, other):
        if not isinstance(other, Auto):
            return "Autos müssen mit anderen Autos dividiert werden"
        try:
            div = self.ps / other.ps
        except ZeroDivisionError:
            div = "Division durch 0 nicht möglich"
        return div

    def __mul__(self, other):
        if not isinstance(other, Auto):
            return "Autos müssen mit anderen Autos multipliziert werden"
        return self.ps * other.ps
    
    def __eq__(self, other):
        if not isinstance(other, Auto):
            return "Autos müssen mit anderen Autos verglichen werden"
        return self.ps == other.ps
    
    def __lt__(self, other):
        if not isinstance(other, Auto):
            return "Autos müssen mit anderen Autos verglichen werden"
        return self.ps < other.ps
    
    def __gt__(self, other):
        if not isinstance(other, Auto):
            return "Autos müssen mit anderen Autos verglichen werden"
        return self.ps > other.ps


def main():

    auto1 = Auto(100)
    auto2 = Auto(10)
    print(auto1 / auto2)
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("A error occured", e)
        sys.exit(1)