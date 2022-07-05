cantidad1=0
cantidad2=0
suma=0
x=1
n_empleados=int(input("ingrese la cantidad de empleados: "))
while x<=n_empleados:
	sueldo=int(input("sueldo que cobra:  "))
	suma=suma+sueldo
	if sueldo>=100 and sueldo<=300:
		cantidad1=cantidad1+1
	else:
		sueldo>300
		cantidad2=cantidad2+1
	x=x+1
	

	
print(" la cantidad de personas que cobran entre 100 y 300 son: ")
print(cantidad1)
print("la cantidad de personas que cobran mas de 300 son: ")
print(cantidad2)
print("la cantidad de dinero que la empresa gasta en sueldos es: ")
print(suma)
