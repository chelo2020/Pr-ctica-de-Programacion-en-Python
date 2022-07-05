cantidad=0
n=int(input("ingrese la cantidad de valores a estudiar: "))
for x in range(n):
	valor=int(input("valores a aplicar: "))
	if valor>=1000:
		cantidad=cantidad+1
		
print("cantidad de  valores mayores o iguales a 1000 es: ")
print(cantidad)