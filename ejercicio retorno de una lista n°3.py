def carga_datos():
    nom=[]
    ed=[]
    for x in range(5):
        nombres=input("ingresar los nombres: ")
        nom.append(nombres)
        edades=int(input("ingresar las edades: "))
        ed.append(edades)
    return [nom,ed]

def mayores_edad(nom,ed):
    print("nombres de las personas mayores de edad")
    for x in range(len(nom)):
        if ed[x]>=18:
            print(nom[x])

def promedio_edades(ed):
    suma=0
    for x in range(len(ed)):
        suma=suma+ed[x]
    promedio=suma//5
    print("la edad promedio de las personas: ")
    print(promedio)

#bloque principal

nombres,edades=carga_datos()
mayores_edad(nombres,edades)
promedio_edades(edades)