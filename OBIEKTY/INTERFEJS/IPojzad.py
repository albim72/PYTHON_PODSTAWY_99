from abc import ABCMeta,abstractmethod

class IPojazd:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def spalanie(self,odl,litry):raise NotImplementedError
    
    @abstractmethod
    def kosztyprzejazdu(self,odl,litry,cena_l):raise NotImplementedError
