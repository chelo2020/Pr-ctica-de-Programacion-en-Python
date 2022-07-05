n=int(input(" cantidad de triangulos a procesar:"))
x=0
cantidad=0
for x in range(n):
	basetri=int(input("ingresar el valor de la base: "))
	alttri=int(input("ingresar el valor de la altura: "))
	superficie=(basetri*alttri)//2
	print("la superficie del triangulo es igual:")
	print(superficie)

if superficie>=12:
	cantidad=cantidad+1
	
print("la cantidad de triangulos que superan la superficie de 12 es: ")
print(cantidad)
	