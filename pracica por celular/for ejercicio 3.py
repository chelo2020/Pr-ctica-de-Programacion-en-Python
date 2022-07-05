mult3=0
mult5=0

for x in range(5):
	num=int(input("ingrese el valor: "))
	if num%3==0:
		mult3=mult3+1
	if num%5==0:
		mult5=mult5+1
		
print("los multiplos de 3 son: ")
print(mult3)
print("los multiplos de 5 son: ")
print(mult5)