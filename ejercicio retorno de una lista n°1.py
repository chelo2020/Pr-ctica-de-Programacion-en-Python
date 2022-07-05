def listado():
    li=[]
    for x in range(5):
        valor=int(input("ingresar los valores: "))
        li.append(valor)
    return li

def listamayor10(li):
    print("los numeros mayore a diez son: ")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])


#bloque principal

lista=listado()
listamayor10(lista)                    