import random
import string


def password(d=12,e= True,f=True,b=True,c=True):
    a =""
    if e:
        a+= string.ascii_lowercase
    if f:
        a+=string.ascii_uppercase
    if b:
        a+=string.digits
    if c:
        a+= string.punctuation

    haslo=''.join(random.choice(a) for _ in range(d))
    return haslo    
if __name__=="__main__":
    try:
        d=int(input("Podaj długość hasła"))
        if d<=0:
            print("coś poszło nie tak: długość misu być większa ni 0")
        else:
            values = ["tak","nie"]
            e = input("Czy używać małych liter? (tak/nie): ").strip().lower()
            while e not in values:
                e = input("Błędna odpowiedź. Czy używać  małych liter? (tak/nie):  ").strip().lower()
            f = input("Czy używać dużych liter? (tak/nie): ").strip().lower()
            while f not in values:
                f = input("Błędna odpowiedź. Czy używać dużych liter? (tak/nie): ").strip().lower()
            b = input("Czy używać cyfr? (tak/nie): ").strip().lower()
            while b not in values:
                b = input("Błędna odpowiedź. Czy używać cyfr? (tak/nie): ").strip().lower()
            c = input("Czy używać znaków specjalnych? (tak/nie): ").strip().lower()
            while c not in values:
                c = input("Błędna odpowiedź. Czy używać znaków specjalnych? (tak/nie): ").strip().lower()
            haslo = password(d,e == "tak", f == "tak", b =="tak", c =="tak")
            print(f"Twoje wygenerowane hasło to: {haslo}")
    except ValueError:
        print("Błąd: podano nieprawidłową wartość (musi być liczba).")




