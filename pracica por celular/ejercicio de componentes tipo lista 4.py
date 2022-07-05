alumnos=[]
notas=[]
x=0

for x in range(3):
    alu=input("ingresar el nombre del alumno: ")
    alumnos.append(alu)
    nota1=int(input("ingresar la primera nota: "))
    nota2=int(input("ingrear la segunda nota: "))
    notas.append([nota1,nota2])

print("las listas son: ")    
print(alumnos)
print(notas)

for x in range(3):
    print(alumnos[x],notas[x][0],notas[x][1])