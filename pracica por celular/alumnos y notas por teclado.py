alumnos=[]
notas=[]

for x in range(3):
	alum=input("ingrese el nombre del alumno: ")
	alumnos.append(alum)
	not1=int(input("ingrese la primer nota:  "))
	not2=int(input("ingrese la segunda nota: "))
	notas.append([not1,not2])
	
print(" la lista de alumnos es: ")
print(alumnos)
for x in range(3):
	print("alumnos y sus respectivas notas y su promedio correspondiente")
	print(alumnos[x],notas[x][0],notas[x][1])
	promedio=(notas[x][0]+notas[x][1])/2
	print( "sus promedio es igual a: ")
	print(promedio)
