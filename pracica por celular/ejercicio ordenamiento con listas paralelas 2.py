paises=[]
habitantes=[]
x=0

for x in range(5):
    pai=input("ingresar el nombre del pais: ")
    paises.append(pai)
    hab=int(input("ingresar cantidad de habitantes: "))
    habitantes.append(hab)

aux=0
aux1=0

for k in range(5):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1

print("ordenamiento alfabeticamente los paises")

for x in range(5):
    print(paises[x],habitantes[x])

for k in range(5):
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1

print(" ordenamiento por cantidad de habitantes")  

for x in range(5):
    print(paises[x],habitantes[x])
