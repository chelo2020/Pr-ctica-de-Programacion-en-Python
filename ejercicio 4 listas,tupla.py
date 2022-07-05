def carga():
    candidatos=[]
    for x in range(3):
        can=input("ingresar su nombre: ")
        prov1=int(input("numero de provincias que debe cargar: "))
        provincias=[]
        for k in range(prov1):
            prov=input("nombre de la provincia: ")
            votos=int(input("ingrese la cantidad de votos: "))
        provincias.append((prov,votos))   
    return  candidatos

def total(candidatos):
    for x in range(len(candidatos)):
        suma=0
        for k in range(len(candidatos[x][1])):
            suma=suma+candidatos[x][1][k][1]
            print(candidatos[x][0])
            print(suma)

#bloque principal

candidatos=carga()
total(candidatos)
