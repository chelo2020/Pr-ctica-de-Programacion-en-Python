x=0
suma=0
valor=0

valor=int(input("ingrese 1 si desea finalizar: "))

while valor!=-1:
    suma=suma+valor
    valor=int(input("ingrese 1 si desea finalizar: "))
    x=x+1

print("la suma de los valores es: ")
print(suma)
