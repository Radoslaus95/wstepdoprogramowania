import random

punkty = [round(random.uniform(0,50),2) for i in range(15)]
print(punkty)

print(f"Najwięcej zdobytych punktów:{max(punkty)},najmniej zdobytych punktów:{min(punkty)}")
liczba = float(input("Podaj liczbę punktów: "))

if liczba in punkty:
    print(punkty.index(liczba))
else:
    print("Liczba nie występuje w liście PUNKTY")

suma = sum(punkty)

średnia = suma/len(punkty)
print(f'średnia punktów:{średnia}')

lista1 =[]
for p in punkty:
    if p > średnia:
        lista1.append(p)
print(lista1,len(lista1))
lista2 = [p for p in punkty if p < średnia]
print(lista2,len(lista2))

