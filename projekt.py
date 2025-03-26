import math#komentarzaaaaaaaaaaaaa
def mnozenie(b,c):
        if b==0:
            print("coś poszlo nie tak")
        elif c==0:
            print("coś poszło nie tak")
        else:
             return b*c 
def trapez(d):
        if d==0:
            print("coś poszło nie tak")
        else:
             return d
a=int(input("Podaj czego chcesz obliczyc pole 1-prostokat,2-trojkat,3-kolo,4-trapez,5-romb,6-rownoległobok"))
if a==1:
    b =int(input("Podaj a"))
    c =int(input("Podaj b"))
    if b<=0:
        print("coś poszło nie tak")
    elif c<=0:
     print("coś poszło nie tak")
    else:
        print(mnozenie(b,c))
if a==2:
    b =int(input("Podaj a"))
    c =int(input("Podaj b"))
    if b<=0:
        print("coś poszło nie tak")
    elif c<=0:
     print("coś poszło nie tak")
    else:
        print(mnozenie(b,c)/2)
if a==3:
    b=int(input("Podaj promien kola"))
    if b<=0:
        print("coś poszło nie tak")
    else:
        print(math.pi*(b**2)) 
if a==4:
    b =int(input("Podaj a"))
    b =int(input("Podaj a"))
    d = int(input("Podaj wysokosc"))
    if b<1:
        print("coś poszło nie tak")
    elif c<=0:
     print("coś poszło nie tak")
    elif d<=0:
        print("coś poszło nie tak")
    else:
        print(((b+c)*trapez(d))/2)
if a==5:        
    b =int(input("Podaj a"))
    c =int(input("Podaj b"))
    if b<=0:
        print("coś poszło nie tak")
    elif c<=0:
     print("coś poszło nie tak")
    else:
        print(mnozenie(b,c)/2)
if a==6:
    b =int(input("Podaj a"))
    c =int(input("Podaj wysokosc "))
    if b<=0:
        print("coś poszło nie tak")
    elif c<=0:
     print("coś poszło nie tak")
    else:
     print(mnozenie(b,c))

      

