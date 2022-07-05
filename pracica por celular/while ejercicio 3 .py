cantidad=0
x=1
piezas=int(input(" cantidad de piezas que va a ingresar: "))
while x<=piezas:
	largo=float(input("ingrese el largo de la pieza"))
	if largo>=1.20 and largo<=1.30:
		cantidad=cantidad+1
	x=x+1

print(" la cantidad de piezas es:  ")
print(cantidad)