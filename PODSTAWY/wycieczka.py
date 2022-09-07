def kwota(t,nw,w,u,i,rab=0):
    return (nw+t)*(1-rab/100)+w+u+i
print(kwota(100,100,50,50,50),"zł")
print(kwota(100,100,50,50,50,25),"zł")

rabs = [0,5,8,12,15,18,20,23,25]

#zbuduj pętlę która wywoła fukcję kwota opartą na liście rabs, podstaw kolejne rabaty z listy rabs.
#dodatkowo stwórz pustą listę wynik = []
#wyełnij listę rozwiązaniami
