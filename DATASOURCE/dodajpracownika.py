import json

def dodaj_nowego_pracownika(new_data,filename = "pracownik.json"):
    with open(filename,"r+") as file:
        file_data = json.load(file)
        file_data["pra_info"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)

nowy_pracownik = {
            "imie": "Jarosław",
            "nazwisko": "Kowalski",
            "stanowisko": "prezes",
            "lata_pracy": 34,
            "email": "jarek@firma.pl"
        }

dodaj_nowego_pracownika(nowy_pracownik)
