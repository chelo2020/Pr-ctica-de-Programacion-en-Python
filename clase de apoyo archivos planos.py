cod_empleado=[]
nombres_apellido=[]
s_basico=[]
categoria=[]
valor=1
x=0

while valor!=0:
    emple=int(input("ingrese el codigo del empleado: "))
    cod_empleado.append(emple)
    nombres=input(" ingrese el nombre del empleado: ")
    nombres_apellido.append(nombres)
    basico=float(input("ingrese el sueldo basico del empleado: "))
    s_basico.append(basico)
    cat=int(input("ingrese 1 si es mecanico o 2 si es conductor: "))
    categoria.append(cat)
    valor=int(input("ingrese 1 si desea seguir o 0 si quiere finalizar la carga: "))
x=x+1
