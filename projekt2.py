import math
def nwd(a,b):
    return math.gcd(a,b)
a=int(input("Podaj pierwszą liczbę"))
b=int(input("Podaj pierwszą liczbę"))

print(f"NWD ({a},{b})= { nwd(a,b)} ")