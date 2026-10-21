def czyparzysta(num: int, num2: int, num3: int):
    czywieksza: bool
    if (num + num2) > num3:
        czywieksza = True
    else:
        czywieksza = False
    print("Czy suma dwóch pierwszych liczb jest większa niż liczba 3?")
    print(czywieksza)
    return(czywieksza)

print("Liczba 1")
liczba1 = input()
print("Liczba 2")
liczba2 = input()
print("Liczba 3")
liczba3 = input()
try:
    liczba1 = int(float(liczba1))
    liczba2 = int(float(liczba2))
    liczba3 = int(float(liczba3))
    czyparzysta(liczba1, liczba2, liczba3)
except:
    print("Podano znak niebędący liczbą!")