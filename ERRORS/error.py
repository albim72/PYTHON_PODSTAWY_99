try:
    wynik = x/2
except NameError:
    print("x nie istnieje!")
except:
    print("nieokreślony błąd!")
else:
    print(f"wynik: {wynik}")
finally:
    x = 7
    print(x)

print("program działa dalej....")
