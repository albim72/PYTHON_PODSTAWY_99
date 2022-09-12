class OldResistor:

    def __init__(self,ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self,ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
print(f"oporność opornika R przed zmianą: {r0.get_ohms()} omów")
r0.set_ohms(10e3)

print(f"oporność opornika R po zmianie: {r0.get_ohms()} omów")
r0.set_ohms(r0.get_ohms()-4e3)
assert r0.get_ohms() == 6e3

class Resistor:

    def __init__(self,ohms):
        self.ohms = ohms
        self.voltage = 0 #napięcie prądu
        self.current = 0 #natężenie prąau


r1 = Resistor(50e3)
r1.ohm1 = 10e3

print(f'oporność: {r1.ohms} omów, napięcie [V]: {r1.voltage}, natężenie [A]: {r1.current}')


class VoltageResistor(Resistor):

    def __init__(self,ohms):
        super().__init__(ohms)
        self._voltage = 0

    #metoda typu getter
    @property
    def voltage(self):
        return self._voltage

    #metoda typu setter

    @voltage.setter
    def voltage(self,voltage):
        self._voltage = voltage
        self.current = self._voltage/self.ohms

r2 = VoltageResistor(25e2)
print(f'natężenie przed przed zmianą: {r2.current:.2f} [A]')
r2.voltage = 250
print(f'natężenie po przed zmianie: {r2.current:.2f} [A]')

class BoundedResistance(Resistor):

    def __init__(self,ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self,ohms):
        if ohms <=0:
            raise ValueError(f"wartość oporności aktualnie -> {ohms} omów musi byc większa niż 0")

        self._ohms = ohms


try:
    r3 = BoundedResistance(1e3)
    r3.ohms = 4
except ValueError as d:
    print(d)
else:
    print(f"oporność: {r3.ohms} [om]")
