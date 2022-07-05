x=1
suma=0 
n1=int(input("ingresar cantidad de valores de la  lista1:  "))

while x<=n1:
	lis1=int(input("ingresar los valores1:  "))
	suma=suma+lis1
	x=x+1

print("la suma de sus valores de la lista1 es: ")
print(suma)

x2=1
suma2=0
n2=int(input("ingresar la cantidad de valores de la lista2 : "))

while x2<=n2:
	lis2=int(input("ingrese los valores de la lista2: "))
	suma2=suma2+lis2
	x2=x2+1
	
print("la suma de los valores de la lista2 es:  ")
print(suma2)

if suma>suma2:
	print(" la lista 1 es mayor a la lista2")
else: 
	print("la lista 2 es mayor a la lista 1")