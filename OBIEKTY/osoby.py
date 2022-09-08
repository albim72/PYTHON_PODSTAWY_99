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
              f" wzrost: {self.wzrost} cm.")
        
    def wiekza10lat(self) -> int:
        return self.wiek+10
    
    def czypracownik(self) -> bool:
        return False
