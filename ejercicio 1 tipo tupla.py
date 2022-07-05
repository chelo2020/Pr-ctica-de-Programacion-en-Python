def carga_fecha():
    dia=int(input("ingrese el dia de su nacimiento: "))
    mes=int(input("ingrese el mes de su nacimiento: "))
    año=int(input("ingrse el año de su nacimiento: "))
    return(dia,mes,año)

def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

#bloque principal

fecha=carga_fecha()
imprimir_fecha(fecha)