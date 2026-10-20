def czyparzysta(num: float):
    parzystosc: bool
    if num%2 == 0:
        parzystosc = True
    elif num%2 == 1:
        parzystosc = False
    else:
        return("Nie liczba!")
    if parzystosc == True:
        print("Liczba Parzysta")
    else:
        print("Liczba Nieparzysta")

print("Liczba")
liczba = input()
try:
    liczba = float(liczba)
    czyparzysta(liczba)
except:
    print("To nie liczba!")