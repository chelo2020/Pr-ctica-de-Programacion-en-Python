empleados=[]
edad=[]

for x in range(2):
	emp=input(" ingrese el nombre del empleado: ")
	empleados.append(emp)
	eda=int(input("ingrese la edad del empleado: "))
	edad.append(eda)
	
print(" los nombres de los empleados es: ")
print(empleados)
print(" la edad de los empleados es: ")
print(edad)

mayor=edad[0]
for x in range(2):
	for x in range(1,2):
		if edad[x]>18:
			mayor=edad[x]
			
print("la persona de mayor edad es: ")
print(mayor)
