def carga_sueldo():
    sueldo=[]
    for x in range(10):
        sue=int(input("ingrese el sueldo del empleado: "))
        sueldo.append(sue)
        print("todos los sueldos son: ")
        print(sueldo)
    return sueldo    

def sueldomayor(sueldo):
    cantidad=0
    for x in range(len(sueldo)):
        if sueldo[x]>4000:
            cantidad=cantidad+1
    print("todos los sueldos mayores a 4000 son: ")        

def promedio(sueldo):
    suma=0
    for x in range(len(sueldo)):
        suma=suma+sueldo[x]
    prom=suma//10
    print("el promedio de sueldos es igual: ")
    print(prom)
    return prom
    

def menorpromedio(sueldo):
    cantidad=0
    for x in range(len(sueldo)):
        if sueldo[x]<prom:
            cantidad=cantidad+1
        print("los sueldos menores al promedio es: ") 
        print(cantidad)      

#bloque principal

sueldo=carga_sueldo()
sueldomayor(sueldo)
promedio(sueldo)
menorpromedio(sueldo)