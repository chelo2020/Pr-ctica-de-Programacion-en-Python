padres=[]
hijos=[]
x=0
cant=0
for k in range(3):
    pa=input("ingrese el nombre del padre: ")
    ma=input("ingrese el nombre de la madre: ")
    padres.append([pa,ma])
    cant=int(input("cantidad de niños que tienen estos padres: "))
    hijos.append([])

    for x in range(cant):
        nom=input("ingrese el nombre del hijo: ")
        hijos[k].append(nom)

print("listado padre,madre e hijos: ")

for k in range(3):
    print("padre: ",padres[x][0])
    print("madre: ",padres[x][1])
    for x in range(len(hijos[k])):
        print("hijo: ", hijos[k][x])

print("listado del padre y cantidad de hijos: ")
for x in range(3):
    print("padre: ", padres[x][0])
    print("cantidad de hijos: ", len(hijos[k]))
    



