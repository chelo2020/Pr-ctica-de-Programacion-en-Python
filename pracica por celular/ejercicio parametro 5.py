def saludo():
    print("BIENVENIDOS AL PROGRAMA DE CARGA")

print("--------------------------------------------")

def ordenar_imprimir(v1,v2,v3):
    if v1<v2 and v1<v3:
        if (v2<v3):
            print(v1,v2,v3)
        else:
            print(v1,v3,v2)
    else:
        if (v2<v3):
            if (v1<v3):
                print(v2,v1,v3)
            else:
                print(v2,v3,v1)
        else:
            if (v1<v2):
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)

def carga_uno():
    valor1=int(input("ingresar un valor: "))
    valor2=int(input("ingresar el segundo valor: "))
    valor3=int(input("ingresar el tercer valor: "))
    ordenar_imprimir(valor1,valor2,valor3)

def finalizacion():
    print("finalizar la carga")

saludo()
carga_uno()
finalizacion()