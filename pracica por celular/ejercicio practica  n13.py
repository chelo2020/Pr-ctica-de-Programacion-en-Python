lista=(12,34,35,5,89)

mayor=lista[0]

for x in range(1,len(lista)):
	if lista[x]>mayor:
		mayor=lista[x]
		
print("el mayor de los cinco numeros es")
print(mayor)