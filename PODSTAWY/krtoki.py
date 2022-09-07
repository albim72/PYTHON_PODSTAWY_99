animal = ("pies","kot","papuga","pies","królik","szczur","pies")
print(animal)
print(animal[1])
print(animal[2:4])
print("________________________")
for a in animal:
    print(a)

print("________________________")

k = animal.index("pies")
print(k)

print(animal.count("pies"))
print(len(animal))

if "papuga" in animal:
    print("tak! papuga to zwierz")

if "most" in animal:
    print("błąd!")

anim2 = ("pająk","ryba")

animal = animal + anim2
print(animal)

mojakrotka = tuple(["obiekt77",False,24677,"Zamość",100.444])
print(mojakrotka)

#Zmodyfikuj krtokę mojakrotka
#usuń wartość 24677, Zamień Zamoć na Gdańsk
#dodaj na końcu wartość 1.1

#zamień krotkę na listę (list()) przerowadź zmiany
#zamień z powrotem listę na krotkę (tuple())

mojalista = list(mojakrotka)
mojalista.remove(24677)
ms = mojalista.index("Zamość")
mojalista[ms] = "Toruń"
mojalista.append(1.1)

mojakrotka = tuple(mojalista)
print(mojakrotka)

pojazd = ('audi','Q7',4.8,2019,76800)
print("model:",pojazd[1])

(marka,model,poj,rocznik,przebieg) = pojazd

print(marka)
print(model)
print(poj)
print(rocznik)
print(przebieg)

