#słownik -> dictionary (klucz,wartość)

pojazd = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1975,
    "przebieg":278900
}

print(pojazd)
print(pojazd["model"])
print(pojazd.get("model"))

pojazd["rocznik"] = 2018

print(pojazd)

pojazd["poj"] = 3.8
print(pojazd)

print(pojazd.items())
print(pojazd.keys())
print(pojazd.values())

print("_____________________________")

for x in pojazd:
    print(x)

print("_____________________________")

for y in pojazd:
    print(pojazd[y])

print("_____________________________")

for k,w in pojazd.items():
    print(w)

print("_____________________________")

for k,w in pojazd.items():
    print(k,":",w)


autokomis = {
                "sam1":{
                        "marka":"Ford",
                        "model":"Mustang",
                        "rocznik":1975,
                        "przebieg":278900
                        },

                "sam2":{
                        "marka":"Opel",
                        "model":"Insignia",
                        "rocznik":2018,
                        "przebieg":67544
                        },
                "sam3":{
                        "marka":"Jeep",
                        "model":"Cherokee",
                        "rocznik":2020,
                        "przebieg":34200
                        }
            }


print(autokomis)
print(autokomis["sam2"])
print(autokomis["sam2"]["rocznik"])
