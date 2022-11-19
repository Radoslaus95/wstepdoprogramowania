# lista = ["ser", "szynka","jogurt","chleb"]
# print(lista[0],lista[1])
# lista[2]= "mleko"
# print(lista)
#
# print(lista[-1],lista[-2])
# print(lista[-2:])

#zadanie 2
import random

zestaw1 = []
n = int(input("Podaj długość listy: "))
for i in range(n):
    z = (random.randint(1, 10))
    zestaw1.append(z)
print(zestaw1)

n=int(input("Podaj długość listy: "))
zestaw2 = [random.randint(5,15) for i in range(n)]
print(zestaw2)

liczba = int(input("Podaj liczbę: "))
if liczba in zestaw1:
    print('Liczba występuje w zestawie 1')
elif liczba in zestaw2:
    print('Liczba występuje w zestawie 2')
else:
    print('Liczba nie występuje w obu zestawach')

zestaw3 = zestaw1+zestaw2

print(zestaw3)
zestaw3.sort()
print(zestaw3)
