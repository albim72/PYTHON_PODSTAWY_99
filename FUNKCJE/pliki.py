import os

f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print("_______________________________________________")
f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()

print("_______________________________________________")

f = open("dane.txt","r",encoding="utf-8")
for linia in f:
    print(linia)
f.close()

print("_______________________________________________")

f = open("message.txt","a",encoding="utf-8")
f.write("to jest istotna wiadomość\n")
f.close()


f = open("message.txt","r",encoding="utf-8")
print(f.read())
f.close()

print("_______________________________________________")

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje")


