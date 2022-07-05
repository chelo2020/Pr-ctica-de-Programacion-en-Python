def castellano():
    diccionario={}
    continua="s"
    while continua=="s":
        cas=input("ingrese la palabra en castellano: ")
        ing=input("ingrese la palabra en inglés: ")
        diccionario[ing]=cas
        continua=input("ingrese si quiere continuar una: s=si o n=no")
    return diccionario

def imprimir(diccionario):
    print("Imprimimos el diccionario completo")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])

def consulta_palabra(diccionario):
    pal=input("ingrese la palabra en ingles que quiera consultar: ")
    if pal in diccionario:
        print("En castellano significa que: ",diccionario[pal])
    else:
        print("La palabra no se encuentra en el Diccionario: ")
        

    

#bloque principal

diccionario=castellano()
imprimir(diccionario)
consulta_palabra(diccionario)
