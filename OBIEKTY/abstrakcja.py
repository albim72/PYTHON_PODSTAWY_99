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
