cantidad=0
cantidad1=0
x=1
n=int(input("cantidad de notas a cargar: "))
while x<=n:
	notas=int(input(" ingresar la nota:  "))
	if notas<7 :
		cantidad=cantidad+1
		print(" no admitido")
	else:
		notas>=7
		cantidad1=cantidad1+1
		print("admitido")
	x=x+1
		
print("cantidad de admitidos")
print(cantidad1)
print("cantidad de no admitidos")
print(cantidad)

		