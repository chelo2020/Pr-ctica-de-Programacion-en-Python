def mostrar_mayor(v1,v2,v3):
    print("el valor mayor de los tres numeros es:")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)

def carga():
    valor1=int(input("ingresar el primer valor: ")) 
    valor2=int(input("ingresar el segundo valor: "))
    valor3=int(input("ingresar el tercer valor: ")) 
    mostrar_mayor(valor1,valor2,valor3)

carga()
