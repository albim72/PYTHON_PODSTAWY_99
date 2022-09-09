class A:

    def mojafunkcja(self):
        print("to jest funkcja klasy A")

class B(A):

    def mojafunkcja(self):
        print("to jest funkcja klasy B")
        super().mojafunkcja()

class C(B):

    def mojafunkcja(self):
        print("to jest funkcja klasy C")
        super().mojafunkcja()


konj = C()

konj.mojafunkcja()
