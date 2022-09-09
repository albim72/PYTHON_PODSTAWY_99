from pojazd import Pojazd

p1 = Pojazd("Jeep","Cherokee",2019,87900,"diesel",4.6,310)

odl = float(input("Podaj odległość [km]: "))
lt = float(input("Podaj liczbę spalonych litrów paliwa: "))
cn = float(input("Podaj cenę litra paliwa [zł]: "))

print(p1.dane_pojazdu())
print(p1.dane_silnika())
print(f"spalanie [l/100km]: {p1.spalanie(odl,lt):.2f}")
print(f"cena przejazdu trasy {odl} km wynosi {p1.kosztyprzejazdu(odl,lt,cn):.2f} zł")
