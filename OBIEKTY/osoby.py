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
    
    def bmi(self):
        return self.waga/(self.wzrost/100)**2
    
    def opisbmi(self):
        if self.bmi() < 18.5:
            return "niedowaga"
        elif self.bmi() <= 25:
            return "waga prawidłowa"
        elif self.bmi() <= 30:
            return "nadwaga"
        else:
            return "otyłość"


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

class Pracownik(Osoba):

    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        print(f"pracownik -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, lata pracy: {self.latapracy}, "
              f"wynagroodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self) -> bool:
        return True

print("______________________________________________________")
e1 = Pracownik("Karol",47,101,173,"ABC","dyrektor",12,11400)
e1.print_osoba()
e1.print_pracownik()
print(e1.wiekza10lat())
print(f'czy osoba jest pracownikiem? {e1.czypracownik()}')


class Sport:
    
    def __init__(self,dyscyplina,lataupr,bestwynik):
        self.dycyplina = dyscyplina
        self.lataupr = lataupr
        self.bestwynik = bestwynik
        
    def infosport(self):
        print(f"dycyplina: {self.dycyplina}, lata uprawiania: {self.lataupr}, życiówka: {self.bestwynik}.")
        
        
class Ekstra:
    pass

class Student(Pracownik,Sport,Ekstra):

    #konstruktor z wielodziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,nr_studenta,kierunek,rok,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lataupr="",bestwynik=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lataupr,bestwynik)
        self.nr_studenta = nr_studenta
        self.kierunek = kierunek
        self.rok = rok

    def print_student(self):
        print(f"dane studenta nr {self.nr_studenta}, kierunek: {self.kierunek}, rok studiów: {self.rok}.")

    def czypracownik(self) -> bool:
        return self.firma != ""


print("______________________________________________________")

s1 = Student("Olaf",22,77,177,34534,"budowa mostów",3)
s1.print_osoba()
s1.print_student()
print(s1.wiekza10lat())
print(f'czy osoba jest pracownikiem? {s1.czypracownik()}')

print("______________________________________________________")

s2 = Student("Paula",23,63,173,675664,"ekonomia",4,"XYZ","sekretarka",1,2500)
s2.print_osoba()
s2.print_student()
s2.print_pracownik()
print(s2.wiekza10lat())
print(f'czy osoba jest pracownikiem? {s2.czypracownik()}')

print("______________________________________________________")

#stwórz instancję Student -> studenta który jest osobą i stuentem oraz sportowcem (ale nie pracownikiem)
#uruchom dostępne metody

s3 = Student("Robert",22,88,182,54545,"informatyka",3,dyscyplina="biegi ultra", lataupr=5, bestwynik="102km 18h15min")
s3.print_osoba()
s3.print_student()
s3.infosport()
print(s3.wiekza10lat())
print(f'czy osoba jest pracownikiem? {s3.czypracownik()}')
