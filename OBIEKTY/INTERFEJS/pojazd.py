from IPojazd import IPojazd
from idane import IDane

class Pojazd(IPojazd,IDane):

    def __init__(self,marka,model,rocznik,przebieg,rodz_silnika,poj,moc):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.przebieg = przebieg
        self.rodz_silnika = rodz_silnika
        self.poj = poj
        self.moc = moc

    def spalanie(self, odl, litry):
        return litry*100/odl

    def kosztyprzejazdu(self, odl, litry, cena_l):
        return self.spalanie(odl,litry)*odl/100*cena_l

    def dane_pojazdu(self):
        return f"Pojazd -> marka: {self.marka}, model: {self.model}, rocznik: {self.rocznik}, " \
               f"przebieg: {self.przebieg}."

    def dane_silnika(self):
        return f"Silnik -> rodzaj silnika: {self.rodz_silnika}, pojemność: {self.poj} l, moc: {self.moc} kM."

