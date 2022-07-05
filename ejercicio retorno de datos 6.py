def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie

print("+++++++++++++++++++++++++++++++++++++++++")
print("primer rectangulo")

lado1=int(input("ingrese el valor de la base del rectangulo: "))
lado2=int(input("ingrese el valor de la altura del rectangulo: "))
print("la superficie del rectangulo es igual a: ")
print(retornar_superficie(lado1,lado2))

print("segundo rectangulo")

lado3=int(input("ingrese el valor de la base del rectangulo: "))
lado4=int(input("ingrese el valor de la altura del rectangulo: "))
print("la superficie del rectangulo es igual a: ")
print(retornar_superficie(lado3,lado4))

if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("los dos rectangulos tienen la misma superficie")
else:
    if retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
        print("el primer rectangulo tiene mayor superficie que el segundo")
    else:
        print("el segundo rectangulo tiene mayor superficie que el primero")




