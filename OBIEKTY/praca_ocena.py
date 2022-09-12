#Stwórz klasę Praca z konstrukotrem opartym na polach: nazwa_pracy, ocena
#stówrz gettery i settery dla obu pól,
#setter dla oceny ma ograniczać możliwość wstawienia oceny spoza zakresu <0,100>
#Stwórz instancję klasy Praca, z zadaniem danych konstrukcyjnych,
#wypisz dane pracy z oceną
# a następnie użyj setterów do wstawienia nowych danych
#oraz getterów do wypisania tych danych


class Praca:

    def __init__(self,nazwa_pracy,ocena):
        self._nazwa_pracy = nazwa_pracy
        self._ocena = ocena

    @property
    def nazwa_pracy(self):
        return self._nazwa_pracy

    @property
    def ocena(self):
        return self._ocena

    @nazwa_pracy.setter
    def nazwa_pracy(self,nazwa_pracy):
        self._nazwa_pracy = nazwa_pracy

    @ocena.setter
    def ocena(self, ocena):
        if not (0<=ocena<=100):
            raise ValueError('ocena musi się zawierać w przedziale <0,100>')
        self._ocena = ocena

    def zmien_dane_pracy(self,nazwa_pracy,ocena):
        self.nazwa_pracy = nazwa_pracy
        self.ocena = ocena



try:
    pr1 = Praca("artykuł naukowy AI01",67)
    print(f'praca: {pr1.nazwa_pracy}, ocena: {pr1.ocena} punktów')
    # pr1.nazwa_pracy = "praca zaliczeniowa nr 06"
    # pr1.ocena = 55
    pr1.zmien_dane_pracy("praca zal 34",135)
    print(f'praca: {pr1.nazwa_pracy}, ocena: {pr1.ocena} punktów')
except ValueError as d:
    print(d)
