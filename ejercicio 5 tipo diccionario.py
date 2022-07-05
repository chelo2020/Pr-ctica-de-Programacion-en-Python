def carga_personas():
    personas={}
    for x in range(4):
        per=input("ingrese su nombre: ")
        DNI=int(input("ingrese su DNI: "))
        personas[DNI]:per
    return personas

def imprimir(personas):
    print("imprimimos las lista completa Nombre-DNI")
    for per in personas:
        print(per,personas[per])

def consulta(personas):
    DNI=int(input("ingrese su DNI: "))
    if DNI in personas:
        print("El DNI pertenece a la persona que lleva por nombre: ")
        print(personas[DNI])
    else:
        print("la persona no esta registrada: ")

#bloque principal

personas=carga_personas()
imprimir(personas)
consulta(personas)            
