#Confeccionar un programa que permita cargar un código 
# de producto como clave en un diccionario. 
# Guardar para dicha clave el nombre del producto,
#  su precio y cantidad en stock.

#Implementar las siguientes actividades:

#1) Carga de datos en el diccionario.

#2) Listado completo de productos.

#3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.

#4) Listado de todos los productos que tengan un stock con valor cero.

def carga():
    Articulos={}
    continuar="s"
    while continuar=="s":
        productos=input("ingresar el nombre del prducto: ")
        precio=float(input("ingresar el precio del producto: "))
        stock=int(input("ingresar el stock del producto: "))
        Articulos[productos]=(precio,stock)
        continuar=input("En el caso de continuar: [s/n] ")
    return Articulos

def imprimir(Articulos):
    print("imprimir el listado de articulos")
    for productos in Articulos:
        print(productos,Articulos[productos][1])

def consulta_producto(Articulos):
    productos=input("ingresar el nombre del producto: ")
    if productos in Articulos:
        print(Articulos[productos][0],Articulos[productos][1])

def stock_cero(Articulos):
    print("los articulos con stock cero son:")
    for productos in Articulos:
        if Articulos[productos][1]==0:
            print(productos,Articulos[productos][0],Articulos[productos][1])


#bloque principal

Articulos=carga() 
imprimir(Articulos)  
consulta_producto(Articulos)
stock_cero(Articulos)