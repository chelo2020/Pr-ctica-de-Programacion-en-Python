nombres=["juan", "marcos", "adriana"]
notas=[[9,8],[6,7],[10,5]]

promedio1=(9+8)/2
promedio2=(6+7)/2
promedio3=(10+5)/2

print("la lista completa de los alumnoses :")
print(nombres)


for x in range(3):
	print(" alumnos y sus respectivas notas: ")
	print(nombres[x],notas[x][0],notas[x][1])


print(" el promedio del primer alumno es: ")
print(promedio1)
print(" el promedio del segundo alumno es :  ")
print(promedio2)
print(" el promedio del tercer alumno es: " )
print(promedio3)