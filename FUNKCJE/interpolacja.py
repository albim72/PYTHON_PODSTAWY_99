wiek = 25
imie = "Olga"
miasto = "Lublin"

osoba = "osoba -> miasto: {}, imię: {}, wiek: {}."
print(osoba.format(miasto,imie,wiek))

osoba = "osoba -> imię: {1}, wiek: {2}, miasto: {0}."
print(osoba.format(miasto,imie,wiek))

print(f"student -> imię:{imie}, wiek: {wiek}, miasto: {miasto}")

ir = "tab77"
wart = 9.6745

formatowanie = '%-30s = %.2f' %(ir,wart)
print(formatowanie)

owoce = [
    ('awokado',4.99),
    ('banany',5.66),
    ('mandarynki',9.67),
    ('maliny',12.23),
    ('jabłka',2.68)
]

#linia cennika -> #nr: nazwa(skok 10 znaków) = cena (2 miejsca po przecinku) zł
print("__________________________________________")
for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(i,nazwa,cena))

print("__________________________________________")


for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(
        i+1,
        nazwa.title(),
        round(cena,1)
    ))
