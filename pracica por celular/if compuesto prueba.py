num1=int(input("ingrese un numero: "))
num2=int(input(" ingrese otro numero: "))
num3=int(input("ingrese otro numero: "))

suma=num1+num2+num3
promedio=suma//3

if promedio>=7:
	print("esta apto")
else:
	if promedio>=4:
		print("no apto")
	else:
		print("deberia recursar")