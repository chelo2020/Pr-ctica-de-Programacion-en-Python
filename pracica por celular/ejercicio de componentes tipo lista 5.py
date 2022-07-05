empleados=[]
sueldo=[]
x=0
totalsueldo=[]

for x in range(3):
    alu=input("ingresar el nombre del empleado: ")
    empleados.append(alu)
    suel1=int(input("ingresar el primer sueldo: "))
    suel2=int(input("ingresar el segunda sueldo: "))
    suel3=int(input("ingresar el tercer sueldo: "))
    sueldo.append([suel1,suel2,suel3])

total=0

for x in range(3):
    total=sueldo [x][0]+sueldo[x][1]+sueldo[x][2]
    totalsueldo.append(total)

for x in range(3):
    print(empleados[x],totalsueldo[x])

posmayor=0
mayor=totalsueldo[0]

for x in range(1,3):
    if totalsueldo[x]>mayor:
        mayor=totalsueldo[x]
        posmayor=x

print("empleados con mayor sueldo: ")
print(empleados[posmayor])
print("el empleado con mayor sueldo es: ")




