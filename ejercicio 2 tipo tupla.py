numeros=(12,34,45)
print("imprimimos la primer tupla")
print(numeros)
listanumeros=list(numeros)
print("imprimimos la lista que se creo por medio de la tupla: ")
print(listanumeros)
listanumeros[0]=67
print("la nueva lista es: ")
print(listanumeros)
an=int(input("ingrese un numero a la lista: "))
listanumeros.append(an)
print("imprima la nueva lista")
print(listanumeros)
numeros2=tuple(listanumeros)
print("la nueva tupla es:")
print(numeros2)


