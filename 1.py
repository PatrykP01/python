'''
liczba=int(input("Podaj liczbe"))
if liczba%2==0:
        print("liczba jest podzielna przez dwa")
elif liczba%2==1:
        print("liczba nie jest podzielna przez dwa")

b=int(input("Podaj liczbe b"))
print(abs(b))

tekst="bardzo dobry tekst"
if "tekst"in tekst:
        print("jest")

for i in range(3):
    print(i)#3
for i in range(1,100):
    print(i)#1-99
for i in range(1,100,2):
    print(i)#1,3,5,7,9,..,99
for i in range(100,0,-1):
    print(i)#99,98,97,96,...,1
for i in "slowo":
    if i=="w":
        break
    print(i)

for i in "slowo":#wypisuje wszystkie litery
    if i=="w":
        continue
    print(i)


liczba=0
while liczba<10:
    print("liczba mniejsza od 10")
    liczba+=1
'''

def powitanie():
    print('cześć')

powitanie()
def powitanie_imienne(imie):
    print('cześć,',imie)
powitanie_imienne("Eryk")



def dzielenie(dzielna,dzielnik):
    if dzielnik==0:
        return
    else:
        return dzielna/dzielnik
print(dzielenie(10,2))
wynik=dzielenie(10,4)
print(wynik)


