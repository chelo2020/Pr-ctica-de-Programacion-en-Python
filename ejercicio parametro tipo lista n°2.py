def mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            lista[x]<men
            men=lista[x]
    print("el mayor de la lista es: ",may)
    print("el menor de la lista es: ",men)    

# Bloque principal

lista=[]
for x in range(5):
    valor1=int(input("ingresar un valor: "))   
    lista.append(valor1)

mayormenor(lista)
