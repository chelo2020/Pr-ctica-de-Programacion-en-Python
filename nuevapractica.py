archivo_texto=open("nuevapractica.txt","w")
archivo_texto.write("segunda opcion")
archivo_texto.write("tercera opcion")
archivo_texto.close()

entrada=open("nuevapractica.txt","r")
suma=0
i=0
for i in entrada.readlines():
    suma=suma+len(i)
    print(suma)
entrada.close()

entrada=open("nuevapractica.txt","r")
suma=0
split=0
palabras=0
x=0
for i in entrada.readlines():
    suma=suma+1
print(suma)
entrada.close()

entrada=open("nuevapractica.txt","r")
suma=0
for i in entrada.readlines():
    palabras=i.split("%")
    suma=suma+len(palabras)
print(suma)
entrada.close()


