from rower import Rower
from osobowy import Osobowy

rw = Rower("Trek","MadOne",2020)
print(rw.pokaz_naped())
print(rw.predkosc_max())

os = Osobowy("Opel","Insignia",2017,"diesel",1.9)
print(os.pokaz_naped())
print(os.predkosc_max())
