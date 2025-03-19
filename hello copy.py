import random
import math




# print ("hello world") #komentarz
# '''
# komentarz blokowy
# '''
# zmienna=10# nazwa=wartość
# tekst='to jest tekst'
# print(zmienna)
# print(type(zmienna))
# print(type(tekst))

# liczba=10.5
# print(type(liczba))

# print('%.10f'%liczba)

# tekst_1='tekst 1'
# tekst_2="tekst2"
# tekst_3="lorem ipsum 'dolor' sit amet"
# print(tekst_3)
# print(tekst_3[1])
# print(tekst_3[-1])
# suma=1+3
# roznica=5-2
# iloczyn=6*4
# iloraz=5/2
# reszta=5%2
# potega=5**2
# nowy_tekst=tekst_1+tekst_2
# print(nowy_tekst)
# ciag=tekst_1*10
# print(nowy_tekst)
# ciag=tekst_1*10
# print(ciag)


# a=10
# print("warto zmiennej a to:", a,".")
# print(f"wartość zmiennej a to :{a}")
# print("Wartość zmiennej a to :"+str(a))


# imie=input("jak masz na imie?")
# print("cześć", imie)
# wiek=int(input("ile masz lat"))
# print(type(wiek))

# los=random.randint(1,10)
# print(los)

# pow=math.pow(2, 5)
# print(pow)

'''
liczba=int(input("Podaj liczbe"))

if liczba>0:
    print("Liczba większa od 0")
elif liczba<0:
    print("Liczba jest mniejsza od 0")
else:
    print("liczba równa 0")


    if liczba!=0:
        print("liczba jest równa od 0")
'''




liczba=int(input("Podaj liczbe"))
if liczba%2==0:
    print("liczba jest podzielna przez dwa")
elif liczba%2==1:
    print("liczba nie jest podzielna przez dwa")

b=int(input("Podaj liczbe b"))
print(abs(b))