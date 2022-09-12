class Film:

    def __init__(self,tytul,producent,cena,opis_filmu,gatunek,imie,nazwisko,biografia):
        self.tytul = tytul
        self.producent = producent
        self.cena = cena
        self.opis_filmu = opis_filmu
        self.gatunek = gatunek
        self.rezyser = Rezyser(imie,nazwisko,biografia) #agregacja na podstawie klasy Rezyser

    def dodajFilm(self):
        return "film dodano"


class Rezyser:

    def __init__(self,imie,nazwisko,biografia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.biografia = biografia

    def bio(self):
        return f"biografia: {self.biografia}"


f = Film("Władca Pierścieni","WB",23,"Film oparty...","Fantasy","Peter","Jackson","...")
print(f.rezyser.bio())

