import math

print("Program wyznacza miejsca zerowe wielomianu stopnia drugiego: ax**2 + bx + c = 0")

def miejsca_zerowa_w2(a,b,c):
    if a==0:
        print("równanie liniowe")
        if b!=0:
            print("jedno miejsce zerowe")
            #bx + c = 0
            x = -c/b
            print(f"wynik: x = {x}")
        elif c!=0:
            print("równanie sprzeczne")
        elif c==0:
            print("nieskończenie wiele rozwiązań")

    else:
        print("wielomian stopnia 2")
        delta = b**2-4*a*c
        if delta < 0:
            print("brak miejsc zerowych")
        elif delta==0:
            print("jedno miejsce zerowe")
            x=-b/(2*a)
            print(f"wynik: x = {x}")
        elif delta >0:
            print("dwa miejsca zerowe")
            x_1 = (-b-math.sqrt(delta))/(2*a)
            x_2 = (-b+math.sqrt(delta))/(2*a)
            print(f"wynik: x_1 = {x_1}, x_2 = {x_2}")

a = float(input("podaj spółczynnik a: "))
b = float(input("podaj spółczynnik b: "))
c = float(input("podaj spółczynnik c: "))

miejsca_zerowa_w2(a,b,c)




