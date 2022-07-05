x=0
print(" Datos de la primera persona")
nombre1=input("ingrese su nombre: ")
edad1=int(input("ingrese su edad: "))
altura1=float(input("ingrese su altura correspondiente: "))

print(" Datos de la segunda persona:")
nombre2=input("ingrese su nombre: ")
edad2=int(input("ingrese su edad: "))
altura2=float(input("ingresu altura: "))

print("El que posee la mayor altura es: ")
if altura1>altura2:
    print(nombre1,altura1)
else:
    print(nombre2,altura2)

