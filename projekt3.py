import math

def nwd(a,b):
    return math.gcd(a,b)
def nww(a,b):
    return abs(a*b) // nwd(a,b)
a=int(input("Podaj pierwszą liczbe"))
b=int(input("Podaj druga liczbe"))
if a<=0 or b<=0:
    print("coś poszło nie tak")
else:
    print(f"NWW({a},{b})= {nww(a,b)}")
