def carga():
    lista=[]
    for x in range(5):
        lista1=int(input("ingrese un numero: "))
        lista.append(lista1)
    return lista
def mayor_menor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]   
        else:
            if lista[x]<menor:
                menor=lista[x]
                
    return (mayor,menor)

# bloque principal
lista=carga()
mayor,menor=mayor_menor(lista)
print("el mayor de la lista", mayor)
print("el menor de la lista", menor)


