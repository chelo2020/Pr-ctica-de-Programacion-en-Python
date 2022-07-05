def producto(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod

#bloque principal

lista=[17,25,34,45]
print("la lista principal es")
print(lista)
print("el producto entre todos los elementos que estan en la lista")
print(producto(lista))