def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista*va
        print(multi)

lista=[3,7,8,9,15]
print("lista original")
print(lista)
print("lista de multiplicar de cada elemento igual a 5: ")
multiplicar(lista,5)
