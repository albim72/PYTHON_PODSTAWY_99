def wersja(kolor,kwota):
    if kolor == "biały":
        return kwota
    elif kolor == "czarny":
        return 1.2*kwota
    elif kolor == "zielony":
        return 1.15*kwota
    else:
        return 0.8*kwota


kol = input("podaj kolor koszulki: ")
cn = float(input("podaj cenę koszulki: "))

print(wersja(kol,cn))


def printlista(lista):
    for element in lista:
        print(element)

w = [34,12,37,8,9,122,4]

printlista(w)
