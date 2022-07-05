def saludos():
    print("BIENVENIDO AL PROGRAMA")

print("--------------------------------------------------")

def mostrar_perimetro(lado):
    per=lado*4
    print("el perimetro es")
    print(per)

def mostrar_superficie(lado):
    sup=lado*lado
    print("la superficie es")
    print(sup)    

def carga_dato():
    la=int(input("ingresar el lado de un cuadrado: "))
    respuesta=input("quiere calclular la superficie o el perimetro[ingresar texto:superficie/perimetr0]: ")
    if respuesta=="perimetro" :
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)

print("------------------------------------------------------------")                

def finalizacion():
    print("CARGA FINALIZADA")

saludos()
carga_dato()
finalizacion()   