def paises_habitantes():
    paises=[]
    for x in range(5):
        pai=input("ingrese el nombre del pais: ")
        hab=int(input("ingrese la cantidad de habitantes del pais ingresado anteriormente: "))
        paises.append((pai,hab))
    return paises

def imprimir(paises):
    print("paises y poblacion")
    for x in range(1,len(paises)):
        print(paises[x][0],paises[x][1])

def paismayor(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("el pais con mayor numero de habitantes es:")
    print(paises[pos],[0])
#bloque principal

paises=paises_habitantes()
imprimir(paises)
paismayor(paises)        

