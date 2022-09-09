from prostokat import Prostokat
from trojkat import Trojkat
from trapez import Trapez
from kolo import Kolo

pr = Prostokat(4.5,6.3)
print(f"pole prostokąta wynosi: {pr.policzpole():.2f} cm2")

tr = Trojkat(4.6,6.2)
print(f"pole trójkąta wynosi: {tr.policzpole():.2f} cm2")

trp = Trapez(8.5,6.1,4.8)
print(f"pole trapezu wynosi: {trp.policzpole():.2f} cm2")

kl = Kolo(5.5)
print(f"pole koła wynosi: {kl.policzpole():.2f} cm2")
