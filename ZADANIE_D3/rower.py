from pojazd import Pojazd
from marka import Marka

class Rower(Pojazd,Marka):

    def __init__(self,nazwa,typ,rocznik):
        super().__init__(nazwa,typ,rocznik)

    def pokaz_naped(self):
        return "korba"

    def predkosc_max(self):
        return 60
