x = lambda a:a+121

print(x(8))
print(x(3.667))
print(x(True))

def policz(a):
    return a+121

print(policz(9))

y = lambda a,b,c=2:(a-b)*c

print(y(4,2.2,5))
print(y(0.0004,12.88,-88.5))
print(y(2,5))

def multi(n):
    return lambda a:a*n

print(multi(5)(23))
d = multi(45)
print(d(11))

liczby = [2,5,17,8,19,45,121,33,36,42,56,77,-4,-7]
#stwórz nową listę -> wparzyste[]  zwierającą tylko wartości parzyste z list liczby
#funkcja filter - standardowa, wysokiego rzędu (parametrem funkcji jest inna funkcja)
wparzyste = list(filter(lambda x:x%2==0,liczby))
print(wparzyste)


#stwórz nową listę -> cube[] mapującą elementy z listy liczby w następujący sposób: x-> x**3
#funkcja map -> standardowa, wysokiego rzędu pozwalająca na odwzorowywanie zbiorów w innych zbiorach danych
cube = list(map(lambda x:x**3,liczby))
print(cube)
