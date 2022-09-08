#słownik z miarami
#dictm -> {1:[przelicznik,nazwa], 2: ....}
#dictm -> {1:[1852,"mila morska"], 2: ....}

#funckja poiczodleglosc(odl_metry,miara):
#jeśli 1 to mila morska
#jeśli 2 to lądowa.....

miary = {
	1: [1852, "mila morska"],
	2: [1609.344, "mila lądowa"],
	3: [0.9144, "jard"],
	4: [0.30477, "stopa"],
	5: [0.0254, "cal"]
}
def policz_odl(metry, jedn):
	if jedn == 1:
		return f"odległość wynosi: {round(metry / miary[1][0], 2)} miara: {miary[1][1]}"
	elif jedn == 2:
		return f"odległość wynosi: {round(metry / miary[2][0], 2)} miara: {miary[2][1]}"
	elif jedn == 3:
		return f"odległość wynosi: {round(metry / miary[3][0], 2)} miara: {miary[3][1]}"
	elif jedn == 4:
		return f"odległość wynosi: {round(metry / miary[4][0], 2)} miara: {miary[4][1]}"
	elif jedn == 5:
		return f"odległość wynosi: {round(metry / miary[5][0], 2)} miara: {miary[5][1]}"
	else:
		return "nie ma takiej miary"
m = float (input ("Podaj odległość w metrach: "))
j = int (input ("Podaj miarę: 1- mila morska, 2 - mila lądowa, "
                "3 - jard, 4 - stopa, 5 - cal: "))
print (policz_odl (m, j))
