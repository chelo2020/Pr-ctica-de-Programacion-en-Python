alturas=[]
x=0
suma=0
promedio=0

for x in range(5):
    alt=float(input("ingrese las alturas correspondientes: "))
    alturas.append(alt)
    suma=suma+alt
promedio=suma/5

print(" el listado de alturas es igual a: ")
print(alturas)
print("el promedio de las altuas es igual a: ")
print(promedio)

suma1=0
suma2=0

for x in range(5):
    if alturas[x]>promedio:
        suma1=suma1+1
    else:
        alturas[x]<promedio
        suma2=suma2+1

print("las personas mal altas son:")
print(suma1)
print("las personas mas bajas son: ")
print(suma2)
    