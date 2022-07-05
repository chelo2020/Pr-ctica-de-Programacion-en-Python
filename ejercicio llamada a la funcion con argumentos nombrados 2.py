# cargar una lista de 10 enteros.
#luego mostrarlos por pantalla a cada
# elemento separados por una coma.

def carga():
    lista=[]
    for x in range(10):
        valor=int(input("ingresar un valor: "))
        lista.append(valor)
    return lista

def imprimir(lista):
    for x in range(len(lista)):
        print([x],end=",")

#bloque principal

lista=carga()
imprimir(lista)    