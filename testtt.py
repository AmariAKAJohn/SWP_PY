class Hund:
    def __init__(self, alter):
        self.alter = alter

class Katze(Hund):
    def __init__(self, alter):
        super().__init__(alter)

# Create an instance of Hund
hund = Hund(10)

# Pass the alter attribute of the Hund instance to Katze
katze = Katze(hund.alter)

# Access the alter attribute of the Katze instance
print(katze.alter)  # Output: 10
