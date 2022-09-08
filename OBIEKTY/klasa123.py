class PierwszaKlasa:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def print_ab(self):
        print(f"a = {self.a}, b = {self.b}")


class DrugaKlasa(PierwszaKlasa):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c

    def print_abc(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")

    def sumuj(self):
        return self.a+self.b+self.c

class Dodatkowa:

    def __init__(self,g):
        self.g = g**2

    def fx(self):
        return 3*self.g - 2

class TrzeciaKlasa(DrugaKlasa,Dodatkowa):

    def __init__(self,a,b,c,d,g):
        DrugaKlasa.__init__(self,a,b,c)
        Dodatkowa.__init__(self,g)
        self.d = d

    def print_abcdg(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, d={self.d}, g = {self.g}")

    def sumuj(self):
        return self.a + self.b + self.c + self.d + self.fx()

print("____________klasa pierwsza______________")
pk = PierwszaKlasa(3,6)
pk.print_ab()
print("____________klasa druga________________")
dk = DrugaKlasa(45,2,8)
dk.print_ab()
dk.print_abc()
print(f"suma a+b+c = {dk.sumuj()}")

print("____________klasa trzecia_______________")

tk = TrzeciaKlasa(6,17,8,19,5)
tk.print_ab()
tk.print_abc()
tk.print_abcdg()
print(f"suma a+b+c+d+fx(g) = {tk.sumuj()}")

#zbuduj klasę Dodatkowa, konsruktor ma być oparty na parametrze g i ma przkazywać kwadrat zadanego parametru
# do zmiennej g, zbuduj dla tej klasy metodę fx -> wynik = 3*g-2
# dodaj do dziedziczenie w TrzeciaKlasa klasę Dodatkowa -> zmień konstruktor z wielodziedziczeniem
#zmodyfikuj metodę print_abcd na print_abcdg -> wyświetl tam dodtkowo g
#zmodyfikuj moeodę sumuj tak aby zwracała -> a+b+c+d + fx(g)

