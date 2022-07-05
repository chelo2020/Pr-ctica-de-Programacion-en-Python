cantidad=0
suma=0
n=int(input(" ingresar la altura promedio de n personas: "))
x=1
while x<=n:
	alturas=float(input("ingresar las alturas"))
	cantidad=cantidad +1
	x=x+1

promedio=suma/n

print("la altura promedio: ")
print(promedio)