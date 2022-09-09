from abc import ABC, abstractmethod

class Prototyp(ABC):

    def __init__(self,x):
        self.x = x

    def info(self):
        print("to jest metoda nieabstrakcyjna klasy abstrakcyjnej")

    @abstractmethod #funkcja dekorująca - wprowadzająca sztywną definicję na funkcję opisaną poiżej
    def policz(self):
        pass

    #dla zasady metoda abstrakcyjna powinna być pusta

    @abstractmethod
    def policz_x(self):
        return self.x*5

    #w tej metodzie zostało użye ciało domyslne metody abstrakcyjnej

class ZwKlasa(Prototyp):

    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 1100

    def policz_x(self):
        return super().policz_x() + 4*self.y


z = ZwKlasa(4,78)
print(f"policz -> {z.policz()}")
print(f"policz_x -> {z.policz_x()}")
z.info()

