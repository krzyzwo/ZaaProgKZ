def funkcja_zad2(x):
    for liczba in x:
        liczba=liczba*2
        print(liczba)

    noweliczby = [liczba*2 for liczba in x]
    print(noweliczby)

funkcja_zad2([1,2,4,8])