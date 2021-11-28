from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = {}

    def tavaroita_korissa(self):
        lukumaara = 0
        for ostos in self.kori.values():
            lukumaara += ostos.lukumaara()
        return lukumaara

    def hinta(self):
        h = 0
        for ostos in self.kori.values():
            h += ostos.hinta()
        return h

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() in self.kori.keys():
            self.kori[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self.kori[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        if poistettava.nimi() in self.kori.keys():
            if self.kori[poistettava.nimi()].lukumaara() > 1:
                self.kori[poistettava.nimi()].muuta_lukumaaraa(-1)
            else:
                del self.kori[poistettava.nimi()]

    def tyhjenna(self):
        self.kori = {}

    def ostokset(self):
        return list(self.kori.values())