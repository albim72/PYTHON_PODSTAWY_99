from pojazd import Pojazd
from marka import Marka
from silnik import Silnik


class Osobowy(Pojazd,Marka,Silnik):

    def __init__(self,nazwa,typ,rocznik,rodzaj,pojemnosc):
        Marka.__init__(self,nazwa,typ,rocznik)
        Silnik.__init__(self,rodzaj,pojemnosc)

    def pokaz_naped(self):
        return "silnik"

    def predkosc_max(self):
        if self.pojemnosc <= 1.0:
            return 140
        elif self.pojemnosc <= 1.5:
            return 170
        elif self.pojemnosc <= 1.8:
            return 190
        elif self.pojemnosc <= 2.2:
            return 210
        elif self.pojemnosc <= 3.0:
            return 240
        else:
            return "pędkość większa niż 240"
