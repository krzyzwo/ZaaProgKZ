def mnozenie(liczb1: int, liczb2: int):
    print(liczb1*liczb2)

print("Liczba 1")
num1 = input()
print("Liczba 2")
num2 = input()
try:
    num1 = int(float(num1))
    num2 = int(float(num2))
    mnozenie(num1, num2)
except:
    print("To nie liczba!")