mecz = "Mecz miesiąca - HIT\nKlub sporotowy: \"Orły Wisła\" - \tTrener: Jan Kot\nlokalizacja: Janowo\nvs\n" \
       "Klub sporotowy: \"Kowale KS\" - \tTrener: Adam Nowak\nlokalizacja: Kowale\n"

print(mecz)

str_ = "       niezwykle ważna i Tajna wiadomość;     RF45434554;    i Tajna PrzEsYłKA"

print(str_)
print(str_.lower())
print(str_.upper())
print(str_.strip())
print(str_.replace("Tajna","Utajniona"))
print(str_.split(";"))

txt = str_.split(";")
for i, ts in enumerate(txt):
       txt[i] = ts.strip()

print(txt)

print(str_.find("Tajna"))
print(str_.strip().find("Tajna"))
print(str_.endswith("ka"))
print(str_.endswith("KA"))

d = "pionierzy"
e = "1002"

print(d.isalpha())
print(e.isdigit())
