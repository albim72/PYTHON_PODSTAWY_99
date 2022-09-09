#stwórz interfejs z metodami abstrakcyjnymi: dane_pojazdu(), dane_silnika() bez parametrów
#zaimplementuj interfejs idane w klasie Pojzad , zbuduj konstruktor dla klasy pozjaxd z polami:
#marka,model,rocznik,przebieg,rodz_silnika,poj,moc
#metoda dane_pojazdu() ma wypisywać dane z konstruktora:  marka,model,rocznik,przebieg
# metoda dane_silnika() ma wypisywać dane z konstruktora:rodz_silnika,poj,moc
#w main.py uzupełnij instancję o obie metody i wy świetl konkretne zadane dane

from abc import ABCMeta,abstractmethod

class IDane:

    __metaclass__ = ABCMeta

    @abstractmethod
    def dane_pojazdu(self):raise NotImplementedError

    @abstractmethod
    def dane_silnika(self):raise NotImplementedError
