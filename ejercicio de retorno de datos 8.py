def archivo(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=="a" or palabra[x]=="A":
            cant=cant+1
    return cant

#bloque principal

palabra=input("ingresar una palabra: ")      
print("la palabra",palabra,"tiene",archivo(palabra),"a")
  