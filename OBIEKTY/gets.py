class Base:

    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

class Child(Base):

    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age

class GrandChild(Child):

    def __init__(self,name,age,city):
        super().__init__(name,age)
        self.city = city

    def get_city(self):
        return self.city


#Napisz klasę Descestor(GrandChild), rozwiń konstruktor o własność wzrost, doddaj metodę get_wzrost,
#Zbuduj nową  isnstancję klasy Descestor i wypisz wszystkie możliwe elementy (4)

class Descestor(GrandChild):

    def __init__(self,name,age,city,wzrost):
        super().__init__(name,age,city)
        self.wzrost = wzrost

    def get_wzorst(self):
        return self.wzrost


osoba = GrandChild("Bonifacy",19,"Kraków")

print(f"Student -> imię: {osoba.get_name()}, wiek: {osoba.get_age()}, miasto: {osoba.get_city()}")

osobad = Descestor("Bonifacy",19,"Kraków",178)

print(f"Student -> imię: {osobad.get_name()}, wiek: {osobad.get_age()}, miasto: {osobad.get_city()}, "
      f"wzrost: {osobad.get_wzorst()}")
