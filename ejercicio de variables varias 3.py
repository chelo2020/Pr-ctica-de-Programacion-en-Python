opcion="si"
suma=0
x=0

while opcion=="si":
    valor=int(input("ingrese un valor: "))
    suma=suma+valor    
    opcion=input("ingrese si o no: ")
    x=x+1


print("la suma total es: ")
print(suma)
