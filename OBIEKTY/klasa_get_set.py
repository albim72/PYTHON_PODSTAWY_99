class Film:

    def __init__(self,tytul,rezyser,rok,gatunek):
        self._tytul = tytul
        self._rezyser = rezyser
        self._rok = rok
        self._gatunek = gatunek


    @property
    def tytul(self):
        return self._tytul

    @property
    def rezyser(self):
        return self._rezyser

    @property
    def rok(self):
        return self._rok

    @property
    def gatunek(self):
        return self._gatunek

    @tytul.setter
    def tytul(self,tytul):
        self._tytul = tytul

    @tytul.setter
    def rezyser(self, rezyser):
        self.rezyser = rezyser

    @tytul.setter
    def rok(self, rok):
        self._rok = rok

    @tytul.setter
    def gatunek(self, gatunek):
        self.gatunek = gatunek


f = Film("ABC","Janek",2010,"Komedia")

print(f"tytuł filmu: {f.tytul}")
f.tytul = "Cienie lasu"
print(f"tytuł filmu: {f.tytul}")
