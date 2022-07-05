def carga():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("ingresar el codigo del producto:"))
        descripcion=input("la descripcion del producto es: ")
        precio=float(input("ingresar el precio del producto: "))
        stock=int(input("ingrese el stock actual del producto: "))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("ingrese una: s, si desea continuar o una n si no desea continuar:"  )
    return productos

def imprimir(productos):
    print("listado completo de los productos: ")  
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2]) 

def consulta(productos):
    codigo=int(input("ingresar el codigo del producto:"))
    if codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])

def stock_cero(productos):
    print("listado de los productos con stock cero")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

# bloque principal

productos=carga()
imprimir(productos)
consulta(productos)
stock_cero(productos)
