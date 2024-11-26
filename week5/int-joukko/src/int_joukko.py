KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti != None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko != None else OLETUSKASVATUS


        self.jono = self._luo_lista(self.kapasiteetti)
        self.len_lista= 0

    def kuuluu(self, n):
        if n in self.jono:
            return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.len_lista >= len(self.jono): 
            uusi_jono = self._luo_lista(len(self.jono) + self.kasvatuskoko)
            self.kopioi_lista(self.jono, uusi_jono)
            self.jono = uusi_jono

        self.jono[self.len_lista] = n
        self.len_lista += 1
        return True

    
    def poista(self, n):
        if n in self.jono: 
            self.jono.remove(n)  
            self.jono.append(0)  
            self.len_lista -= 1 
            return True
        return False

    def kopioi_lista(self, a, b):
        b[:len(a)] = a

    def mahtavuus(self):
        return self.len_lista

    def to_int_list(self):
        taulu = self.jono[:self.len_lista]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        jonojen_yhdiste = IntJoukko()
        for i in a.to_int_list() + b.to_int_list():
            jonojen_yhdiste.lisaa(i)
        return jonojen_yhdiste

    @staticmethod
    def leikkaus(a, b):
        jonojen_leikkaus = IntJoukko()
        for i in a.to_int_list():
            if i in b.to_int_list():
                jonojen_leikkaus.lisaa(i)
        return jonojen_leikkaus

    @staticmethod
    def erotus(a, b):
        jonojen_erotus = IntJoukko()
        for i in a.to_int_list():
            if i not in b.to_int_list():
                jonojen_erotus.lisaa(i)
        return jonojen_erotus

    def __str__(self):
        return "{" + ", ".join(map(str, self.jono[:self.len_lista])) + "}"