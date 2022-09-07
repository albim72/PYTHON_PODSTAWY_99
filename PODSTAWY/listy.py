kraj = ["Polska","Niemcy","Włochy","Hiszpania","Kanada","Chiny"]

print(kraj)
print(kraj[1])
print(kraj[2:4])
kraj.append("Turcja")
print(kraj)
kraj[3] = "Francja"
print(kraj)

kraj.sort()
print(kraj)

kraj.reverse()
print(kraj)

kraj.sort(reverse=True)
print(kraj)

mojeid = kraj.index("Kanada")
print(mojeid)

liczby = [2,67,88,100,0,-12,112,0,15,12,12,90,999,-222,112,0,112]
liczby.sort(reverse=True)
print(liczby)

liczby.remove(112)
print(liczby)

moje = liczby.index(67)
print(moje)
del liczby[moje]
print(liczby)

print(liczby[3:6])

sklepzoo = [["pies","kot","papuga","mysz","szynszyla"],[6500,2300,8900,45,250]]

#CTRL+D -> powielenie linii
print(sklepzoo[0])
print(sklepzoo[0][2],"cena:",sklepzoo[1][2],"zł")

miasto = ["Toruń","Kraków","Poznań"]
stolica = ["Warszawa","Wilno","Londyn"]

miasto = miasto + stolica #konkatenacja tablic
print(miasto)

odejmij = ["Wilno"]

# miasto = miasto - odejmij
# print(miasto)

#CTRL + /    komentowanie istniejących linii kodu

miasto = miasto*3

print(miasto)

litery = ['a','b','c','d','e','f','g','h']
print("litery przed zmianą:",litery)

litery[2:7] = [34,99,11]
print("litery po zmianie:",litery)

litery_m = litery
litery_p = list(litery)
litery_q = litery[:]

print("litery przed zmianą:",litery)
print("litery_m przed zmianą:",litery_m)

litery[:] = [1001,1002,1100,1110]

print("litery po zmianie:",litery)
print("litery_m po zmianie:",litery_m)
print("litery_p po zmianie:",litery_p)
print("litery_q po zmianie:",litery_q)

kolory = ['czerwony','niebieski','biały','czarny','zielony','szary']
#stwórz dwie nowe tablice: parz i nieparz
#do tablicy parz przekaż wszystkie elementy listy kolory, kótre posiadają parzyste indeksy położeń
#do tablicy nieparz przekaż wszystkie elementy listy kolory, kótre posiadają nieparzyste indeksy położeń

parz = kolory[::2]
nieparz = kolory[1::2]

print(parz)
print(nieparz)

t1 = "kajak"
t2 = "pomarańcza"

#wypisz wyrazy wspak
t1w = t1[::-1]
t2w = t2[::-1]
print(t1,t1w)
print(t2,t2w)
