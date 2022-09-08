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
    
class TrzeciaKlasa(DrugaKlasa):
    
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d = d

    def print_abcd(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, d={self.d}")

    def sumuj(self):
        return self.a + self.b + self.c + self.d

    print("____________klasa pierwsza______________")
pk = PierwszaKlasa(3,6)
pk.print_ab()
print("____________klasa druga________________")
dk = DrugaKlasa(45,2,8)
dk.print_ab()
dk.print_abc()
print(f"suma a+b+c = {dk.sumuj()}")

print("____________klasa trzecia_______________")

tk = TrzeciaKlasa(6,17,8,19)
tk.print_ab()
tk.print_abc()
tk.print_abcd()
print(f"suma a+b+c+d = {tk.sumuj()}")
