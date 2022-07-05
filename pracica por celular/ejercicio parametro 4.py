def cantidad_vocales(cadenas):
    cant=0
    for x in range(len(cadenas)):
        if cadenas[x]=="a" or cadenas[x]=="e" or cadenas[x]=="i" or cadenas[x]=="o" or cadenas[x]=="u":
            cant=cant+1
        print("la cantidad de vocales que tiene", cadenas, "es",cant)

#bloque principal

cantidad_vocales("juanmarcelo")
cantidad_vocales("adriana")
cantidad_vocales("maestra")
