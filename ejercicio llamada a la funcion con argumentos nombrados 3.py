def tabla(nombre, termina=10):
    for x in range(termina):
        valor=x*nombre
        print(valor,",",sep="",end="")
    print()

#bloque principal

print("tabla del 6")
tabla(6)
print("tabla del 6 con 8 terminos")
tabla(6,8)
tabla(termina=8,nombre=6)