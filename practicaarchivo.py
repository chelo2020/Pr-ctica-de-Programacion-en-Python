archivo=open("hello.txt","w")
archivo.write("hola")
archivo.close()

lista=[10,15,24]
archivo=open("practicaarchivo.txt","w")
archivo.write(lista)
archivo.write("\n")
suma=lista[0]+lista[1]
archivo.write(suma)
print(" la suma de las dos primeras componentes es")
print(suma)
archivo.close()
raw_input=0

salida=open("practicaarchivo.txt","a")
salida.write(input(" ingrese una frase"))
salida.close()

entrada=open("practicaarchivo.txt","r")
print(entrada.read())
entrada.close()


