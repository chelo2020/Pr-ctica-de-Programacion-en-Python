lista=[230,255,300,450]
x=0
cantidad=0

while x<len(lista):
    if lista[x]>200:
        cantidad=cantidad+1
x=x+1
print(lista)
print(cantidad)