lista=[]
x=0
opcion=0
num=int(input("ingresar los valores: "))

while num!=0:
    lista.append(num)
    num=int(input("ingrese 0 si quiere finalizar la carga: "))
x=x+1
print(" la lista tiene un tamaño de: ")
print(len(lista))    
