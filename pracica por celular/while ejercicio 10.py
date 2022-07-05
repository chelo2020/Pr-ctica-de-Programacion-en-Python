x=1
n=0
pares=0
impares=0

n_cantidad=int(input("ingrese la cantidad de valores que va a necesitar: "))

while x<=n_cantidad:
	lista=int(input("ingrese la cantidad de valores: "))
	if lista%2:
		pares=pares+1
		
	else:
		impares=impares+1
		
	x=x+1
	
print("numeros impares")
print(impares)
print("numeros pares")
print(pares)
	
	
	
	

		
		
			
			