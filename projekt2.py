import math

def nwd(a,b):
    return math.gcd(a,b)
a=int(input("Podaj pierwszą liczbę"))
b=int(input("Podaj pierwszą liczbę"))
if a<=0 or b<=0:
    print("coś poszło nie tak")
else:
    print(f"NWD ({a},{b})= { nwd(a,b)} ")