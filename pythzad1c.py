def funkcja_zad3(y):
    for liczba in y:
        if liczba%2 == 0:
            print(liczba)

liczby = []
for i in range(10):
    liczby.append(i+1)
funkcja_zad3(liczby)