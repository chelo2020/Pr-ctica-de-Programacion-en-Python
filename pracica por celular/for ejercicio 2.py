x=0
aprobados=0
desaprobados=0
cantidad=0
for x in range(5):
	notas=int(input("ingresar las notas: "))
	if notas>=7:
		aprobados=aprobados+1
	else:
		desaprobados=desaprobados+1
		
print(" los aprobados son: ")
print(aprobados)
print("los desaprobados son: ")
print(desaprobados)
	