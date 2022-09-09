import json

json_str = '{"name":"Jan","age":34,"city":"Toruń"}'
print(json_str)
print(type(json_str))

dane_osoba = json.loads(json_str)
print(dane_osoba)
print(type(dane_osoba))
print(dane_osoba["city"])

samochod = {
    "marka":"Audi",
    "model":"Q7",
    "poj":4.6,
    "silnik":"diesel"
}

jsonsam = json.dumps(samochod,indent=4)
print(jsonsam)
print(type(jsonsam))

#plikiem żródeł json jest plik nazwa.json
with open("jsonsam.json","w",encoding="utf-8") as f:
    f.write(jsonsam)

with open("jsonsam.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
print(type(auto_dict))

print("******************************************************")

info = '{"organizacja":"Fundacja BIOTECH","miasto":"Krosno","kraj":"Polska"}'

ekstra = {"id":45343,"zakres":"sztuczna inteligencja"}

#dołącz słownik do źródła JSON

z = json.loads(info)
z.update(ekstra)

info_new = json.dumps(z)
print(info_new)
