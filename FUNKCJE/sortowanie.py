mojenazwy_classic = ['samolot','marchewka','mecz','miecz','Mieczysław','zenit','piorun','macierz','apokryf',
                     'Anna','123']
def mlitery(lista):
    for i,elem in enumerate(lista):
        lista[i] = elem.lower()
    return lista

def bsort_classic(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i]<a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

bsort_classic(mlitery(mojenazwy_classic))
print(mojenazwy_classic)


mojenazwy_modern = ['samolot','marchewka','mecz','miecz','Mieczysław','zenit','piorun','macierz','apokryf',
                     'Anna','123']

def bsort_modern(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i]<a[i-1]:
                a[i-1],a[i] = a[i],a[i-1]

bsort_modern(mlitery(mojenazwy_modern))
print(mojenazwy_modern)
