alumnos=[]
notas=[]
x=0

for x in range(5):
    alu=input("ingrese el nombre de los alumnos: ")
    alumnos.append(alu)
    nota=int(input("ingrese la nota correspondiente: "))
    notas.append(nota)
print(alumnos[x],notas[x])

aux=0
aux1=0
for k in range(5):
    for x in range(4-k):
        if notas[x]<notas[x+1]:
            aux=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux
            aux1=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux1

print("el listado ordenado de mayor a menor")
for x in range(5):
    print(alumnos[x],notas[x])