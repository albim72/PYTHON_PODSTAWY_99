class Kolor:

    #opis stanu - konstruktor klasy
    def __init__(self,id,nazwa):
        self.idkoloru = id # zmienna -> parametr
        self.nazwa = nazwa
        self.paleta = "paleta A"

    #zachowane-funkcje klasy -> metody

    def print_kolor(self):
        print(f'kolor: {self.nazwa}, id koloru: {self.idkoloru}, paleta: {self.paleta}')


k1 = Kolor(2,"czerwony")
k1.print_kolor()

k2 = Kolor(99,"czarny")
k2.paleta = "paleta X"
k2.print_kolor()

k1.print_kolor()
