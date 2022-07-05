paises=[]
habitantes=[]
x=0
aux1=0
aux2=0

for x in range(5):
    pai=input("ingresar nombres de paises: ")
    paises.append(pai)
    hab=int(input("ingrese la cantidad de habitantes del País: "))
    habitantes.append(hab)

for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2
            
            

print(" los paises son: ")

for x in range(5):
    print(paises[x],habitantes[x])

print("ordenamiento por cantidad de habitantes")

for x in range(4):
    for k in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2
            

print("los paises ordenados por cantidad de habitantes: ")
for x in range(5):
    print(paises[x],habitantes[x])