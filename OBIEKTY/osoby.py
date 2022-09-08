class Osoba:

    def __init__(self,imie:str,wiek:int,waga:float,wzrost:float):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.info()

    def info(self) -> None:
        print("Tworzenie nowej instancji klasy Osoba -> obiekt Osoba")

    def print_osoba(self) -> None:
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek} lat, waga: {self.waga} kg,"
              f" wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}")

    def wiekza10lat(self) -> int:
        return self.wiek+10

    def czypracownik(self) -> bool:
        return False


p1 = Osoba("Jan",45,112,174)
p1.print_osoba()
print(p1.wiekza10lat())
print(f'czy osoba jest pracownikiem? {p1.czypracownik()}')

print("______________________________________________________")

p2 = Osoba("Olga",24,54,168)
p2.kolor_oczu = "niebieskie"
p2.print_osoba()
print(p2.wiekza10lat())
print(f'czy osoba jest pracownikiem? {p2.czypracownik()}')

