def witaj(name):
    return f"Witaj {name}!"

def konkurs(name,points):
    return f"Uczestnik konkursu: {name} - liczba punktów: {points}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))

print(osoba(konkurs,"Olga",45))

print("___________________________________________________")

def gratulacje(jesli):

    def gratuluj():
        return "Brawo!Gratuluję zdanego egzaminu!"
    def szkoda():
        return "Przykro mi!Następnym razem będzie lepiej!"

    if jesli == "tak":
        return gratuluj
    else:
        return szkoda

print(gratulacje("tak")())
print(gratulacje("nie")())


print("__________________funkcja dekorująca___________________")

def startstop(funkcja):
    def wrapper():
        print("startowanie procesu....")
        funkcja()
        print("kończenie procesu....")
    return wrapper


def zawijanie():
    print("zwijanie czekoladek w sreberka...")

zaw = startstop(zawijanie)
zaw()

@startstop
def krecenie():
    print("kręcenie bączków...")

krecenie()
