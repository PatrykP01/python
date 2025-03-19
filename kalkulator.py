def dzielenie(a,b):
        if b==0:
            print("coś poszlo nie tak")
        else:
            return a/b
def mnozenie(a,b):
    return a*b
def dodawac(a,b):
    return a+b
def odejmowac(a,b):
    return a-b
def dzieleniezreszta(a,b):
    if b==0:
        print("Cos poszlo nie tak")
    return a%b
def potegowanie(a,b):
    return a**b
a=int(input("Podaj liczbe"))
b=int(input("Podaj liczbe"))
wybor=int(input("Czy chcesz dzielic 0=tak,1=nie"))
if wybor==0:
        print(dzielenie(a,b))

elif wybor==1:
    wybor1=int(input("Czy chcesz mnozyc 0=tak,1=nie"))
    if wybor1==0:
       
        print(mnozenie(a,b))
if wybor1==1:
    wybor2=int(input("Czy chcesz dodawac 0=tak ,1=nie"))
    if wybor2==0:
        print(dodawac(a,b))
if wybor2==1:
    wybor3=int(input("Czy chcesz odejmowac 0=tak,1=nie"))
    if wybor3==0:
        print(odejmowac(a,b))
if wybor3==1:
    wybor4=int(input("Czy chcesz dzielic z reszta 0=tak,1=nie"))
    if wybor4==0:
        print(dzieleniezreszta(a,b))
if wybor4==1:
    wybor5=int(input("Czy chcesz potegowac 0=tak,1=nie"))
    if wybor5==0:
        print(potegowanie(a,b))
if wybor5==1:
    print("Program wiecej nieobsluguje")





    