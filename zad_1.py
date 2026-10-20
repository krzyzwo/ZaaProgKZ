def imie(name: str, surname: str) -> str:
    fullname = f'Cześć {name} {surname}!'
    print(fullname)

print("Imie")
name1 = input()
print("Nazwisko")
name2 = input()
imie(name1, name2)