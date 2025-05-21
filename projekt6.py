
def ok(a,b, c):
    # Wszystkie jednostki w metrach
    jednostki = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344
    }
    b = b.lower()
    c= c.lower()
    if b not in jednostki or c not in jednostki:
        return "Nieznana jednostka."
    d = a * jednostki[b]
    e = d / jednostki[c]
    return e
try:
        a = float(input("Podaj wartość do przekształcenia: "))
        b= input("Podaj jednostkę, z której chcesz przekształcić (np. km, m, ft, in, yd, mi,): ").strip()
        c = input("Podaj jednostkę, na którą chcesz przekształcić (np. km, m, ft, in, jd, mi): ").strip()
        f = ok(a, b, c)
        print(f"{a} {b} to {c}: {f}")
except ValueError:
        print("Wprowadź poprawną wartość liczbową.")
        
