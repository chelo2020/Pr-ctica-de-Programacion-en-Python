def lista_palabras():
    palabras=[]
    for x in range(3):
        nombres=input("ingrese su nombre: ")
        palabras.append(nombres)
    return palabras

def palabra_caracteres(palabras):
    print("la palabra con mayor cantidad de caracteres es: ")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra)

#bloque principal

palabras=lista_palabras()
palabra_caracteres(palabras)            

