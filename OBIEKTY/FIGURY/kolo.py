import math
from figura import Figura

#napisz klasę Kolo(Figura)
#zdefinuj konstruktor dla koła z uwzględnieniem promienia koła
#zaimplementuj metodę policzpole() -> pole koła -> pi*promien**2
# pi -> math.pi
# w pliku main.py policz pole koła dla promienia -> 5.5

class Kolo(Figura):

    def __init__(self,a):
        super().__init__(a,0)

    def policzpole(self):
        return math.pi*self.a**2
