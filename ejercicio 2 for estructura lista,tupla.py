def carga():
    lista=[]
    for x in range(5):
        lis=int(input("ingrese el numero entero: "))
        lista.append(lis)
    return lista

def imprimir(lista):
    print("la lista completa es: ")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    mayor=lista[0]
    for elemento in lista:
        if elemento>mayor:
            mayor=elemento
    print("el mayor de la lista es: ")
    print(mayor)

def sumar_elementos(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("la suma de todos sus elementos es: ")
    print(suma)

#bloque principal

lista=carga()
imprimir(lista)
mayor(lista)
sumar_elementos(lista)    
