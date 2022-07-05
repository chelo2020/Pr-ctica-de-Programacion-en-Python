lista=[]
elementos=int(input("cuantos elementos tendra la lista: "))
sublista=int(input("cantidad de elementos que tendra la sublista" ))

for k in range(elementos):
    lista.append([])
    for x in range(sublista):
        valor=int(input("ingrese un valor: "))
        lista[k].append(valor)

print(lista)

suma=0

for x in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma + lista[k][x]

print(suma)        