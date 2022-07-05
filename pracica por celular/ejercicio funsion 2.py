def carga_suma():
	valor1=int(input("ingresar el primer valor: "))
	valor2=int(input("ingresar el segundo valor: "))
	suma=valor1+valor2
	print("la suma de los valores es: ")
	print(suma)
	
def separacion():
	print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

for x in range(3):
	carga_suma()
	separacion()