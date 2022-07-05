def suma(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


# bloque principal

print("la suma de 1+7")
print(suma(1,7))
print("la suma de 2+5+7+9")
print(suma(2,5,7,9))
        