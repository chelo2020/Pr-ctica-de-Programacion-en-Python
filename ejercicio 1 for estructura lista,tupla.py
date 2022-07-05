# si queremos modificar una variable de la lista
# debemos proceder de la siguiente manera

lista=[9,8,12,6,8]

for x in range(len(lista)):
    if lista[x]<10:
        lista[x]=0

print(lista)