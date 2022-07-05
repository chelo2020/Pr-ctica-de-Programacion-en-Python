lista=[[2,2,3,4],[3,5,7,8]]

suma1=lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]
suma2=lista[1][0]+lista[1][1]+lista[1][2]+lista[0][3]

print(suma1)
print(suma2)

#utilizando un for
print("sumando usando un ciclo for")

suma1=0
for x in range(len(lista[0])):
    suma1=suma1+lista[0][x]
    print(suma1)

suma2=0
for x in range(len(lista[1])):
    suma2=suma2+lista[1][x]
    print(suma2)

    
