def cargar():
    empleados=[]
    for x in range(5):
        nombre=input("ingrese el nombre del empleado: ")
        sueldo=int(input("ingrese su sueldo correspondiente: "))
        empleados.append((nombre,sueldo))
    return empleados    

def imprimir(empleados):
    print("empleados y sus empleados")
    for nombre,sueldo in empleados:
        print(nombre,sueldo)


def mayor_sueldo(empleados):
    empleado=empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado=emp
    print("empleados con mayor sueldo es: ")
    print(empleado[1])

def sueldo_menor1000(empleados):
    cant=0
    for empleado in empleados:
        if empleado[1]<1000:
            cant=cant+1
    print("el empleado con el sueldo menor a 1000 es:")
    print(cant)

#bloque principal


empleados=cargar()
imprimir(empleados)
mayor_sueldo(empleados)
sueldo_menor1000(empleados)        

