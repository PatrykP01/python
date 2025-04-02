import math
def nwd(a,b):
    return math.gcd(a,b)
def nww(a,b):
    return abs(a*b) // nwd(a,b)
a=int(input("Podaj pierwszą liczbę"))
b=int(input("Podaj pierwszą liczbę"))
print(f"NWW({a},{b})= {nww(a,b)}")

