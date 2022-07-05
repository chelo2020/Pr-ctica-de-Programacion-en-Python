def carga_empleado():
    empleado=[]
    sueldo=[]
    for x in range(1):
        empleado1=input("ingresar el nombre del empleado: ")
        empleado.append(empleado1)
        sueldo1=float(input("ingresar el sueldo: "))
        sueldo.append(sueldo1)
    return (empleado,sueldo)

def mayor_sueldo(empleado1,empleado2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0],"tiene mayor sueldo")
    else:
        print(empleado2[0],"tiene menor sueldo") 

# bloque principal

empleado1=carga_empleado()
empleado2=carga_empleado()
mayor_sueldo(empleado1,empleado2)   

