def czyzawiera(lista: list[int], wartosc: int):
    zawiera: bool = False
    for number in lista:
        if number == wartosc:
            zawiera = True
    if zawiera:
        print("Wartość zawiera się w liście!")
    else:
        print("Wartość nie zawiera się w liście!")

czyzawiera([2,4,6,1,3], 7)