empleados1=[]
empleados2=[]
x=0
sueldos=0

print("ingresar los sueldos del turno mañana")

for x in range(4):
    sueldos=int(input("ingresar su sueldo: "))
    empleados1.append(sueldos)
print(empleados1)

print("ingresar los sueldos del turno tarde")

for x in range(4):
    sueldos=int(input("ingresar su sueldo: "))
    empleados2.append(sueldos)

print(empleados2)