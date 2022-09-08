import csv

with open("firma.csv",encoding="utf-8") as pc:
    csv_reader = csv.reader(pc,delimiter=";")
    licznik_wierszy = 0
    for wiersz in csv_reader:
        if licznik_wierszy == 0:
            print(f'nazwa kolumny: {", ".join(wiersz)}')
            licznik_wierszy += 1
        else:
            print(f'\t{wiersz[0]} pracuje na stanowisku {wiersz[1]} i ma urodziny w miesiącu: '
                  f'{wiersz[2]}, otrzymuje nagrodę w wysokości: {wiersz[3]} zł')
            licznik_wierszy += 1

    print(f'dodano {licznik_wierszy} linii')
    print(f'dodano {licznik_wierszy-1} osób')
