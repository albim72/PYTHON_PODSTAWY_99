#n! = 1*2*...*n, gdzie należy do liczb całkowitych nieujemnych
#double -> max -> 1.8E+308 (10**308)
#n?? 171
import sys
def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość n argumentu funkcji silnia: "))
    sys.setrecursionlimit(100000)
    print(f"silnia z {n} wynosi: {silnia(n)}")
    print(f"silnia rekurencyjna z {n} wynosi: {silnia_rek(n)}")
except ValueError as d:
    print(d)
except:
    print("totalnie nieznany błąd!")
    raise
