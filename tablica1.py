import time 
n=int(input("podaj liczbe calkowita:"))
start=time.time()
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()
end=time.time()
print(end-start)