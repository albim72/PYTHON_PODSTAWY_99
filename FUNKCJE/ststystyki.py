liczby = [56,78,79,90,89,12,-55,88,101,45,23,48,92,102,-77]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    return minimum,maksimum,rozstep

wynik = pokaz_stat(liczby)
print(wynik)

mini,maxi,roz = pokaz_stat(liczby)

print(f"wartość maksymalna: {maxi}, wartość minimalna: {mini}, rozstęp danych: {roz}")
