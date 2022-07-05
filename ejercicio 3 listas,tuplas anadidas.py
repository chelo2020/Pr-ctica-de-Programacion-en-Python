def carga_empleados():
    empleados=[]
    for x in range(5):
        emp=input("ingrese los empleados de la empresa: ")
        sue1=float(input("ingrese su sueldo: "))
        sue2=float(input("ingrese su sueldo: "))
        sue3=float(input("ingrese su sueldo: "))
        empleados.append([emp,(sue1,sue2,sue3)])
    return empleados

def ganancias_empresa(empleados):
    print("el total que le empresa abono por los empleados es: ")
    for x in range(5):
        total=  empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0])
        print(total)

def ganancias_mayores(empleados):
    print("el empleado con mayor a 10000 es: ")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print("el sueldo es de: ")
            print(empleados[x][0])
            print(total)


#bloque principal
empleados=carga_empleados()    
ganancias_empresa(empleados)
ganancias_mayores(empleados)
