kat=int(input("Podaj kat"))

while kat<0:
    kat1=int(input("Nie ma takiego kata,Podaj kat miedzy 0 a 361"))
    if kat1==360:
        print("kat jest pelny")
    elif kat1==90:
        print("kat jest prosty")
    elif kat1==180:
        print("kat jest polpelny")
    elif 0<kat1<90:
        print("kat jest ostry")
    elif 90<kat1<180:
        print("kat jest rozwarty")
    elif 180<kat1<360:
        print("kat jest wklesly")
        