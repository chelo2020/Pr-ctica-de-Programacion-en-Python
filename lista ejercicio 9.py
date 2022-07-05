x=0
suma=0
promedio=0
sueldos_operarios=[]

for x in range(5):
    sueldos=float(input("ingrese su sueldo"))
    sueldos_operarios.append(sueldos)
    suma=suma+sueldos
promedio=suma/5
print("la lista de sueldos es igual a: ")
print(sueldos_operarios)
print(" el promedio de los sueldos es igual: ")
print(promedio)


