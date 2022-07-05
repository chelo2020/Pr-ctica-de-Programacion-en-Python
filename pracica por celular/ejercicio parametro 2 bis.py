def comienzo(mensaje):
	print("***************************")
	print(mensaje)
	print("***************************")
	
def mostrar(v1,v2,v3):
	print("mostrar el mayor de los valores:  ")
	if v1>v2 and v1>v3:
		print(v1)
	else:
		if v2>v3:
			print(v2)
		else:
			print(v3)
			
def carga():
	valor1=int(input("ingresar el primer valor: "))
	valor2=int(input("ingresar el segundo valor: "))
	valor3=int(input("ingresar el tercer valor:" ))
	mostrar(valor1,valor2,valor3)
	
comienzo(" BIENVENIDO AL PROGRAMA")
carga()
comienzo("FIN DEL PROGRAMA")