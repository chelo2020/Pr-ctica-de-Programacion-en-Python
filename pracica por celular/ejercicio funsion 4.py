def carga_menor():
	valor1=int(input("ingrese su primer valor: "))
	valor2=int(input("ingrese en zegundo valor: "))
	valor3=int(input("ingrese en tercer valor: "))
	if valor1<valor2 and valor1<valor3:
		print("el menor  es")
		print(valor1)
	else:
		if valor2<valor3:
			print(valor2)
		else:
			print("el menor es")
			print(valor3)
			
carga_menor()