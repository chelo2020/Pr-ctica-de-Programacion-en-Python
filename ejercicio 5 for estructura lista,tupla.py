def carga_producto():
    producto=[]
    for x in range(5):
        nombre=input("ingrese el nombre del producto:")
        precio=float(input("ingrese el precio del producto"))
        producto.append((nombre,precio))
    return producto

def imprimir(producto):
    print("imprimir la lista nombres y precio de los productos")
    for nombre,precio in producto:
        print(nombre,precio)

def precios(producto):
    print("el listado de los productos entre 10 y 15 son:")
    for nombre,precio in producto:
        if precio>=10 and precio<=15:
            print(nombre,precio)


#bloque principal

producto=carga_producto()
imprimir(producto)
precios(producto)