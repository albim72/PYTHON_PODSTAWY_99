def podziel(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("dzielenie przez zero!")
    except NameError:
        print("brak zmiennej")
    except TypeError:
        print("Użyto ciąg str. W dzieleniu używaj tylko liczb!")
    else:
        print(f"wynik dzielenie: {wynik}")
    finally:
        print("policzmy coś jeszcze....")

try:
    podziel(4,5)
    podziel(4,0)
    podziel(0,0)
    podziel(-9.55,0.0004)
    podziel(56,False)
    podziel(2000,True)
    podziel("fffffff",8)
    podziel(56)
except TypeError:
    print("podaj właściwą liczbę argumentów funkcji!")
