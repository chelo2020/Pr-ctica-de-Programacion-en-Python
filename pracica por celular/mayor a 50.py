numeros=[]
for x in range(4):
	num=int(input("ingresar un valor: "))
	numeros.append(num)
	
print( " la lista de numeros es: ")
print(numeros)

print(" la cantidad de elementos que tiene la lista es: ")
print(len(numeros))

mayor=0
menor=0

for x in range(4):
	if numeros[x]>50:
		mayor=numeros[x]	
	if numeros[x]<50:
		menor=numeros[x]
	
print(" el mayor numero de 50 es: ")
print(mayor)
print("el menor numero de 50 es: ")
print(menor)
	
	
	