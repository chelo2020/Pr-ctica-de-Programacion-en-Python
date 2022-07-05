num1=int(input("ingresar un numero: "))
num2=int(input("ingresar otro numero: "))
num3=int(input("ingresar otro numero: "))

if num1>num2:
	if num1>num3:
		print(num1)
	else:
		print(num3)
	
else: 
	if num2>num3:
		print(num2)
	else: 
		print(num3)