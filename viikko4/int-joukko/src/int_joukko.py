
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int):
            raise Exception("Kapasiteetti ei ole kokonaisluku")
        elif kapasiteetti < 0:
            raise Exception("Kapasiteetti on negatiivinen")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int):
            raise Exception("Kasvatuskoko ei ole kokonaisluku")
        elif kasvatuskoko < 0:
            raise Exception("Kasvatuskoko on negatiivinen")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.lukumaara = 0

    def kuuluu(self, n):
        if n in self.lukujono:
            return True

        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        self.lukujono[self.lukumaara] = n
        self.lukumaara += 1

        if len(self.lukujono) > 0:
            self.lukujono += [0] * self.kasvatuskoko

        return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False

        del self.lukujono[self.lukujono.index(n)]
        self.lukumaara -= 1

        return True

    def mahtavuus(self):
        return self.lukumaara

    def to_int_list(self):
        taulu = [0] * self.lukumaara

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste_int_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste_int_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste_int_joukko.lisaa(b_taulu[i])

        return yhdiste_int_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_int_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_int_joukko.lisaa(b_taulu[j])

        return leikkaus_int_joukko

    @staticmethod
    def erotus(a, b):
        erotus_int_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus_int_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_int_joukko.poista(b_taulu[i])

        return erotus_int_joukko

    def __str__(self):
        merkkijono = "{" + str(list(filter(lambda merkki: merkki != 0, self.lukujono)))[1:-1] + "}"
        return f'{merkkijono}'
