import math 
lista=[1,2,3,4,5,6]


a=int(input("Podaj czego objętość chcesz liczyć: 1=czworościan foremny,2=ostrosłup czworokątny,3=stozek,4=walec,5=kula,6=sześcian"))
if a in lista:
    if a==1:
        b=int(input("Podaj długość podstawy"))
        c=int(input("Podaj wysokość"))
        if b<=0:
            print("coś poszło nie tak")
        elif c<=0:
            print("coś poszło nie tak")
        else:
            print(((b**2)*c)/3)
    if a==2:
        b=int(input("Podaj długość podstawy "))
        c=int(input("Podaj długość drugiej bok podstawy  "))
        d=int(input("Podaj wysokość"))
        if b<=0:
            print("coś poszło nie tak")
        elif c<=0:
            print("coś poszło nie tak")
        elif d<=0:
            print("coś poszło nie tak")
        else:
            print(((a*b)*d)/3)
    if a==3:
        b=int(input("Podaj  długość promień podstawy"))
        c=int(input("Podaj wysokość"))
        if b<=0:
            print("coś poszło nie tak")
        elif c<=0:
            print("coś poszło nie tak")
        else:
            print((((b**2)*math.pi)*c)/3)
    if a==4:
        b=int(input("Podaj długość promienia podstawy"))
        c=int(input("Podaj wysokość"))
        if b<=0:
            print("coś poszło nie tak")
        elif c<=0:
            print("coś poszło nie tak")
        else:
            print((b**2)*math.pi)
    if a==5:
        b=int(input("Podaj długość promienia podstawy"))
        if b<=0:
            print("coś poszło nie tak")
        else:
            print((((b**3)*math.pi)*4)/3)
    if a==6:
        b=int(input("Podaj długość boku"))
        if b<=0:
            print("coś poszło nie tak")
        else:
            print(b**3)
else:
    print("coś poszło nie tak")
    



        

 