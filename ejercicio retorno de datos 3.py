def largo(cadena):
    return len(cadena)

#bloque principal

nombre1=input("ingrese un nombre: ")
nom1=largo(nombre1)
nombre2=input("ingrese otro nombre: ")
nom2=largo(nombre2)
if nom1==nom2:
    print("los nombres,nombre1,nombre2,tienen la misma cantidad de caracteres")
else:
    if nom1>nom2:
        print("nom1, es el mas largo")
    else:
        print("nom2, es el mas largo")    
        

