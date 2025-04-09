#konwenter jednostek
a=int(input("Co chcesz przekonwertować 1=długośći , 2=masę czy3=litry"))
values=[1, 2, 3]
print("Coś poszło nie tak")
while a not in values :
    a=int(input("Co chcesz przekonwertować 1=długośći , 2=masę czy3=litry"))
if a==1:
    b=int(input("Z czego chcesz przekonwertować\ncentymetry\n" \
    "1=z centymetrów na metry\n" \
    "2= z centymetrów na kilometry\n" \
    "3=z centymetrów na decymetry\n" \
    "4=z centymetrów na cale\n" \
    "5=z centymetrów na stopy\n" \
    "6=z centymetrów na jardy\n" \
    "7=z centymetrów na mile\nMetry\n" \
    "8=z metrów na centymetry\n" \
    "9=z metrów na kilometry\n" \
    "10=z metrów na decymetry\n" \
    "11=z metrów na cale\n" \
    "12=z metrów na stopy\n" \
    "13=z metrów na jardy\n" \
    "14=z metrów na mile\nkilometry\n" \
    "15=z kilometrów na centymetry\n" \
    "16=z kilometrów na metry"))

    #cale (inches), stopy (feet), jardy (yards) i mile (miles)