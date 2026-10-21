def listowanie(lista1: list[int], lista2: list[int]):
    for element in lista2:
        lista1.append(element)
    lista1 = list(dict.fromkeys(lista1))
    licz = 0
    for element1 in lista1:
        lista1[licz] = element1 ** 3
        licz = licz+1

    print("ok")
    print(lista1)

listowanie([1,5,8,2],[6,4,3,2])