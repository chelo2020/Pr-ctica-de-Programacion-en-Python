numeros=[]
for x in range(5):
	num=int(input(" ingrese un numero: "))
	numeros.append(num)
	
print(" la lista de numeros es: ")
print(numeros)

menor=numeros[0]
posicion=0

for x in range(5):
	if numeros[x]<menor:
		menor=numeros[x]
		posicion=x
print("el menor de los numeros es:  ")
print(menor)
print(" su posicion en la lista es: ")
print(posicion)
		