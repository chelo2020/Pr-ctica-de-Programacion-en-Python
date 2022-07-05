x=0
lado1=0
lado2=0
lado3=0
equilatero=0
isosceles=0
escaleno=0
n=int(input("ingrese la cantidad de triangulos a trabajar"))

for x in range(n):
    lado1=int(input("ingresar su valor: "))
    lado2=int(input("ingresar su valor: "))
    lado3=int(input("ingresar su valor: "))
    if lado1==lado2==lado3:
        equilatero=equilatero+1
    if lado1==lado2!=lado3:
        isosceles=isosceles+1
    if lado1!=lado2!=lado3:
        escaleno=escaleno+1
print("la cantidad de triangulos equilateros es: ")
print(equilatero)
print("la cantidad de triangulos isosceles es: ")
print(isosceles)
print("la cantidad de triangulos escalenos es: ")
print(escaleno)
        
        