def listado():
    li=[]
    for x in range(5):
        valor=int(input("ingresar el valor: "))
        li.append(valor)
    return li

def lista(li):
    may=li[0]
    men=li[0]
    for x in range(len(li)):
        if li[x]>may:
            may=li[x]
            
        else:
            li[x]<men
            men=li[x]
    return [may,men]        
#bloque principal

lista1=listado() 
rango=lista(lista1)
print("el mayor de los numeros es: ",rango[0])
print("el menor de los numeros es: ",rango[1])
         

