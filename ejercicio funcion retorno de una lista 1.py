def lista():
    lis=[]
    for x in range(10):
        lis1=int(input("ingresar un numero: "))
        lis.append(lis1)
    return lis
def imprimir(lis):
    print("imprimir lis=sueldos")
    for x in range(len(lis)):
        print(lis[x])

def mayora4000(lis):
    may=0
    cant=0
    for x in range(len(lis)):
        if lis[x]>4000:
            cant=cant+1
    print("cantidad de sueldos mayores a 4000")
    print(cant)

def promedio(lis):
    suma=0
    for x in range(len(lis)):
        suma=suma+lis[x]
        promedio=suma//10
    return promedio

def sueldosbajos(lis):
    pro=promedio(lis)
    print("los sueldos por debajo del promedio general es")
    print(pro)
    for x in range(len(lis)):
        if lis[x]<pro:
            print(lis[x])

#bloque principal

lis=lista()
imprimir(lis)
mayora4000(lis)
sueldosbajos(lis)                   



