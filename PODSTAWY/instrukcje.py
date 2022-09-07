a=0
b=0

if a>b:
    print("a jest więsze niż b")
elif a == 0 and b==0:
    print("a i b wynoszą 0")
elif a==b:
    print("a jest równe b")
else:
    print("a jest mniejsze niż b")


#iteracja

i = 1
while i<6:
   print(i)
   if i == 3:
       break
   i+=1
else:
    print("i wynosi:",i)


owoce = ["jabłko","śliwka","truskawka","banan","cytryna","kiwi"]
print(owoce)

for owoc in owoce:
    print(owoc)

print("_____________________________________________")

cechy = ["kolorowy","elegancki","kosztowny","brudny","zniszczony"]
obiekty = ["ogród","samochód","budynek","przystanek","płaszcz"]

for cecha in cechy:
    for obiekt in obiekty:
        print(cecha,obiekt)
