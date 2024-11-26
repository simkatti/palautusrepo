class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
class Erotus:
    def __init__(self, sovelluslogiikka, operandi):
        self._sovelluslogiikka = sovelluslogiikka
        self._operandi = operandi
        self._edellinen_arvo = 0
        
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        uusi_arvo = self._sovelluslogiikka.arvo() - int(self._operandi())
        self._sovelluslogiikka.aseta_arvo(uusi_arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Summa:
    def __init__(self, sovelluslogiikka, operandi):
        self._sovelluslogiikka = sovelluslogiikka
        self._operandi = operandi 
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        uusi_arvo = self._sovelluslogiikka.arvo() + int(self._operandi())
        self._sovelluslogiikka.aseta_arvo(uusi_arvo)
    
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.aseta_arvo(0)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


