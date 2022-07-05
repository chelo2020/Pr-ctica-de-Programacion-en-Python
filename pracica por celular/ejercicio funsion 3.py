def presentacion():
	print("programa de carga de valores ")
	print("----------------------------------------------")
	
def parte1():
	print("el cuadrado de un numero ")
	
	valor=int(input("ingrese un valor: "))
	cuadrado=valor**2
	print("el cuadrado del numero es: ")
	print(cuadrado)
	
def parte2():
	print("el producto de dos numeros")
	
	valor1=int(input("ingresd el primer valor: "))
	valor2=int(input("ingrese el segundo valor: "))
	producto=valor1*valor2
	print("el producto de los dos valores es: ")
	print(producto)
	
print("--------------------------------------------------")

def finalizacion():
	print("finalizo el programa: ")
	print("-----------------------------------------------")
#programa principal

presentacion()
parte1()
parte2()
finalizacion()
