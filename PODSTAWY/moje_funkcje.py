def witaj():
    print("witaj użytkowniku")
    print("zapłać abonament")
    print("zaloguj się")


witaj()
witaj()

for _ in range(1,26):
    witaj()

#funckja druga
print("Funkcja obywatel -> wyświetla dane mieszkańca wybranego kraju....")

def obywatel(nrtelefonu,kraj="Polska"):
    print("Pochodzę z kraju:",kraj,", nr telefonu:",nrtelefonu)

obywatel(543534534,"Norwegia")
obywatel(7654654645,"Francja")
obywatel(243565656,"Kanada")
obywatel(675456466,"Peru")
obywatel(323243656)

#funkcja trzecia
print("Funkcja policz() -> zwraca wynik oblienia arytmetycznego")

def gx(n):
    return n**3-1

f = 100
def policz(a,b,x):
    global f
    f = (a+b)*x + f + gx(b)
    return f

print(policz(7,3,1))
print(f)

print(policz(0.55,100,45))
print(policz(0.000056,0.0000343,23))
print(policz(True,1000,False))

#funkcja czwarta

def miasta(miasto3,miasto2="Kielce",miasto1="Kraków"):
    print("miasto tygodnia:",miasto1,", drugie miejsce:",miasto2,",trzecie miejsce:",miasto3)


miasta("Toruń","Poznań","Zamość")
miasta("Toruń","Poznań")
miasta("Toruń")
miasta("Gliwice",None,"Gdańsk")
miasta("Gliwice",miasto1="Gdańsk")

#funckja piąta

def zamki(id,*zamek,rabat):
    print("zamek tygodnia:",zamek[0],"rabat:", rabat,"zł, drugie miejsce:",zamek[1],",trzecie miejsce:",zamek[2])

zamki(1,"Malbork","Czersk","Olsztyn",rabat=20)
zamki(3,"Janowiec","Malbork","Czersk","Będzin","Olsztyn",rabat=5)



