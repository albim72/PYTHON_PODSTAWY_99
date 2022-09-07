drzewa = {"buk","jesion","dąb","sosna","baobab","jabłoń","grusza"}

print(drzewa)
print(drzewa)
print(drzewa)

print("___________________________________")
for d in drzewa:
    print(d)
print("___________________________________")

print("jesion" in drzewa)
print("osika" in drzewa)

drzewa.add("osika")
print(drzewa)

drzewa.update(["topola","wierzba","świerk","czereśnia"])

print(drzewa)

liczby = [2,3,4,2,3,4,5,6,5,4,3,2,3,2,4,5,2,3,4,5]
unikaty = set(liczby)
liczby = list(unikaty)

print(liczby)

drzewa.remove("topola")
print(drzewa)

drzewa.discard("jojoba")
print(drzewa)

drzewa.discard("sosna")
print(drzewa)

m = drzewa.pop()
print(m)
print(drzewa)
