#konwenter długości

a=int(input("Co chcesz przekształcać\n"
    "1-centymetry\n"
    "2-metry\n"
    "3-kilometry\n"
    "4-cale\n"
    "5-stopy\n"
    "6-jardy\n"
    "7-mile\n"
    "wpisz numer:"))
value=[1,2,3,4,5,6.7]
while a not in value:
            a=int(input("Z czego chcesz przekonwertować\n"
    "1-centymetry\n"
    "2-metry\n"
    "3-kilometry\n"
    "4-cale\n"
    "5-stopy\n"
    "6-jardy\n"
    "7-mile\n"
    "wpisz numer:"))
if a==1:
        a=int(input("Jak chcesz przkształcać\n"
        "1-z centymetrów na metry\n"
        "2-z centymetrów na kilometry\n"
        "3-z centymetrów na cale\n"
        "4-z centymetrów na stopy\n"
        "5-z centymetrów na jardy\n"
        "6-z centymetrów na mile"))
        value=[1,2,3,4,5,6.]
while a not in value:
                a=int(input("Jak chcesz przkształcać\n"
        "1-z centymetrów na metry\n"
        "2-z centymetrów na kilometry\n"
        "3-z centymetrów na cale\n"
        "4-z centymetrów na stopy\n"
        "5-z centymetrów na jardy\n"
        "6-z centymetrów na mile\n"
        "Podaj numer:"))
if a==1:
        try:
            b= input("Podaj ile masz centymetrów ma być liczba całkowita: ")
            number = int(b)  
            print(number * 0.01)
        except ValueError:
            b=int(input("Podaj ile masz centymetrów ma być liczba całkowita:"))
        print(b*0.01)
if a==2:
        try:
            b= input("Podaj ile masz centymetrów ma być liczba całkowita: ")
            number = int(b)  
            print(number * 0.001)
        except ValueError:
            b=int(input("Podaj ile masz centymetrów ma być liczba całkowita:"))
        print(b*0.001)
if a==3:
        try:
            b= input("Podaj ile masz centymetrów ma być liczba całkowita: ")
            number = int(b)  
            print(number * 0.39)
        except ValueError:
            b=int(input("Podaj ile masz centymetrów ma być liczba całkowita:"))
        print(b*0.39)
if a==4:
        try:
            b= input("Podaj ile masz centymetrów ma być liczba całkowita: ")
            number = int(b)  
            print(number * 0.03281)
        except ValueError:
            b=int(input("Podaj ile masz centymetrów ma być liczba całkowita:"))
        print(b*0.03281)
if a==5:
        try:
            b= input("Podaj ile masz centymetrów ma być liczba całkowita: ")
            number = int(b)  
            print(number * 0.0109)
        except ValueError:
            b=int(input("Podaj ile masz centymetrów ma być liczba całkowita:"))
        print(b*0.0109)
if a==6:
        try:
            b= input("Podaj ile masz centymetrów ma być liczba całkowita: ")
            number = int(b)  
            print(number * 0.000006)
        except ValueError:
            b=int(input("Podaj ile masz centymetrów ma być liczba całkowita:"))
        print(b*0.000006)
if a==2:
        a=int(input("Jak chcesz przekształcać\n"
        "1-z metrów na centymetry\n"
        "2-z metrów na kilometry\n"
        "3-z metrów na cale\n"
        "4-z metrów na stopy\n"
        "5-z metrów na jardy\n"
        "6-z metrów na mile\n"))
        value=[1,2,3,4,5,6.]
while a not in value:
    a=int(input("Jak chcesz przekształcać\n"
        "1-z metrów na centymetry\n"
        "2-z metrów na kilometry\n"
        "3-z metrów na cale\n"
        "4-z metrów na stopy\n"
        "5-z metrów na jardy\n"
        "6-z metrów na mile\n"
        "Podaj numer:"))
if a==1:
    try:
            b= input("Podaj ile masz metrów ma być liczba całkowita: ")
            number = int(b)  
            print(number *100)
    except ValueError:
            b=int(input("Podaj ile masz metrów ma być liczba całkowita:"))
    print(b*100)
if a==2:
    try:
            b= input("Podaj ile masz metrów ma być liczba całkowita: ")
            number = int(b)  
            print(number *0.1)
    except ValueError:
            b=int(input("Podaj ile masz metrów ma być liczba całkowita:"))
    print(b*0.1)
if a==3:
    try:
            b= input("Podaj ile masz metrów ma być liczba całkowita: ")
            number = int(b)  
            print(number *39.37)
    except ValueError:
            b=int(input("Podaj ile masz metrów ma być liczba całkowita:"))
    print(b*39.37)
if a==4:
    try:
            b= input("Podaj ile masz metrów ma być liczba całkowita: ")
            number = int(b)  
            print(number *3,2808)
    except ValueError:
            b=int(input("Podaj ile masz metrów ma być liczba całkowita:"))
    print(b*3.2808)
if a==5:
    try:
            b= input("Podaj ile masz metrów ma być liczba całkowita: ")
            number = int(b)  
            print(number *1.0936)
    except ValueError:
            b=int(input("Podaj ile masz metrów ma być liczba całkowita:"))
    print(b*1.0936)
if a==6:
    try: 
        b= input("Podaj ile masz metrów ma być liczba całkowita: ")
        number = int(b)  
        print(number *0.0006)
    except ValueError:
        b=int(input("Podaj ile masz metrów ma być liczba całkowita:"))
    print(b*0.0006)
if a==3:
    a=int(input("Jak chcesz przekształcać\n"
    "1-z kilometrów na centymetry"))
