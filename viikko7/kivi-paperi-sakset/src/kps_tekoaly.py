from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self) -> None:
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        return tokan_siirto

