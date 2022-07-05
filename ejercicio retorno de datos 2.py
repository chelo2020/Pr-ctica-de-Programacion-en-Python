def retornar(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor

valor1=int(input("ingresar el primer valor: "))
valor2=int(input("ingresar el segundo valor: "))
print(retornar(valor1,valor2))


