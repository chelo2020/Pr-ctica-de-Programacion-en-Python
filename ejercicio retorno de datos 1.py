def mensaje(mensaje):
    print("+++++++++++++++++++++++++++++++++++++")
    print(mensaje)
    print("+++++++++++++++++++++++++++++++++++++")

def retorno_superficie(lado):
    sup=lado*lado
    return sup

va=int(input("ingrese el valor del lado del cuadrado: "))
superficie=retorno_superficie(va)

print(" la superficie del cuadrado es: ")
print(superficie)

