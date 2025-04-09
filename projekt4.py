import random
import string


def password(d=12,b=True,c=True):
    a=string.ascii_letters
    if b:
        a+=string.digits
    if c:
        a+= string.punctuation

    haslo=''.join(random.choice(a) for _ in range(d))
    return haslo    
if __name__=="__main__":
    d=int(input("Podaj długość hasła"))
    b=input("Czy uzywać cyfr?(tak/nie):").strip().lower()
    c=input("Czy uzywać znaków specjalnych(tak/nie):").strip().lower()
    values=["tak", "nie"]
    print("Coś poszło nie tak!")
    while b not in values or c not in values:
        b=input("Czy uzywać cyfr?(tak/nie):").strip().lower()
        c=input("Czy uzywać znaków specjalnych(tak/nie):").strip().lower()
    haslo=password(d,b,c)
    print(f"Twoje wygenerowane hasło to{haslo}")





