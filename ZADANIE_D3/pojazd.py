from abc import ABC, abstractmethod

class Pojazd(ABC):

    @abstractmethod
    def pokaz_naped(self):raise NotImplementedError

    @abstractmethod
    def predkosc_max(self):raise NotImplementedError
