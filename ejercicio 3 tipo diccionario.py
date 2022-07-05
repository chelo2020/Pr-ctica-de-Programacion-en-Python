def almacenar():
    articulos={}
    for x in range(5):
        nombre=input("ingrese el nombre de los productos: ")
        precio=int(input("ingrese loa valores: "))
        articulos[nombre]=precio
    return articulos


def imprimir(articulos):
    print("listado de todos los articulos")
    for nombre in articulos:
        print(nombre,articulos[nombre])

def imprimir_mayor100(articulos):
    print("vemos los articulos mayores de 100")
    for nombre in articulos:
        if articulos[nombre]>100:
            print(nombre)

#bloque principal

articulos=almacenar()
imprimir(articulos)
imprimir_mayor100(articulos)

