def articulos_precios():
    articulos=[]
    precio=[]
    for x in range(5):
        nombres=input("ingresar el nombre del rpoducto: ")
        articulos.append(nombres)
        pre=int(input("ingresar el precio del articulo: "))
        precio.append(pre)
    return [articulos,precio]

def imprimir(articulos,precio):
    print("los articulos y sus precios: ")
    for x in range(len(articulos)):
        print(articulos[x],precio[x])

def mayor_precio(articulos,precio):
    mayor=precio[0]
    pos=0
    for x in range(1,len(precio)):
        if precio[x]>mayor:
            precio[x]=mayor
            pos=x
    print("el articulo con mayor precio",articulos[pos],"su precio es", mayor)

def consulta_precio(articulos,precio):
    valor=int(input("ingrese un precio para saber si es menor: "))
    for x in range(len(precio)):
        if precio[x]<valor:
            print(articulos[x],precio[x])

#bloque principal

articulos,precio=articulos_precios()
imprimir(articulos,precio)
mayor_precio(articulos,precio)
consulta_precio(articulos,precio)