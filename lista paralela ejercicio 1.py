alumnos=[]
notas=[]
x=0

for x in range(5):
    alum=input("ingresar su nombre: ")
    alumnos.append(alum)
    nota=int(input("ingresar sus notas: "))
    notas.append(nota)

aux=0
aux1=0

for k in range(5):
    for x in range(k-4):
        if notas[x]<notas[x+1]:
            aux=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux
            aux1=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux1


print("las listas ordenadas: ")
    
for x in range(5):
    print(alumnos[x],notas[x])