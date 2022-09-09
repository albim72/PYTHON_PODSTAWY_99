from pojazd import Pojazd

p1 = Pojazd()

odl = float(input("Podaj odległość [km]: "))
lt = float(input("Podaj liczbę spalonych litrów paliwa: "))
cn = float(input("Podaj cenę litra paliwa [zł]: "))

print(f"spalanie [l/100km]: {p1.spalanie(odl,lt):.2f}")
print(f"cena przejazdu trasy {odl} km wynosi {p1.kosztyprzejazdu(odl,lt,cn):.2f} zł")
