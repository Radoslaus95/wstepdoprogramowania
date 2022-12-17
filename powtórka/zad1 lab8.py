def find(lista,a):
    lista2=[]
    for x  in range(len(lista)):
        if lista[x]==a:
            lista2.append(x)
    return lista2
lista=[53,23,5,6,34,46,2,1,23,6,2]
a=0
d=find(lista,a)
print(d)
g=find(["A","B","C","D","E","F","G"], "D")
print(g)