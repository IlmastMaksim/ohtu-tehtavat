from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.arvo = 0

    def suorita(self):
        self.arvo = self.syote()
        arvo = int(self.arvo)
        self.sovelluslogiikka.plus(arvo)
    
class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.arvo = 0

    def suorita(self):
        self.arvo = self.syote()
        arvo = int(self.arvo)
        self.sovelluslogiikka.miinus(arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.kumoa()


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote)
        }

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)
    
    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)
        self._tulos_kentta = ttk.Label(textvariable=self._tulos_var)
        self._summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )
        self._erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )
        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )
        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )
        self._tulos_kentta.grid(columnspan=4)
        self._syote_kentta.grid(row=1, columnspan=4)
        self._summa_painike.grid(row=2, column=0)
        self._erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=3, column=0)
        self._kumoa_painike.grid(row=3, column=1)