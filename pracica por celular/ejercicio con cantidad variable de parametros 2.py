def lista():
    lis=[12,25,46,34]
    cant=0
    for x in range(len(lis)):
        if lis[x]>=18:
            cant=cant+1
            print(cant)
    return cant

print("los mayores o iguales a 18 son: ")
#bloque principal

lista()    
