#Carga de datos de personas (Alta de personas)

#1) Cargar los datos que exista en el archivo 
# persona.dat en un dicionario. 

#2) Se ingresa la clave (código de persona). 
# Si la clave es cero, se sale de programa. 
# Si la clave no es cero, se accede al Diccionario
#   y se verifica que la misma exista. 
# En caso de que exista la clave, 
# se emite un mensaje “No se puede dar de alta, 
# clave ya existe. Sólo puede modificar o borrar.”

#En el caso de que la clave no exista, 
# se procede a cargar y guardar la información 
# necesaria en el archivo persona.dat

#Ingresar el Apelldo y nombre: 
# (no puede superar 30 caracteres de longitud).

#El sexo (1=Varon, 2=Mujer) verificar  
# si el valon ingresado es correcto. 
# Si se ingresó un valor incorrecto, 
# imprimir en pantalla “Prestá atención”.

#Ingresar el Importe (No puede ser cero)

#Se ingresa la sucursal : 1=Posadas  2=Garupa 
# 3- Candelaria. Nuevamente, 
# si se ingresa un valor incorrecto, 
# imprimir “Prestá Atención.”

#Cuando ingresa la sucursal, buscar en una tupla, 
# la sucursal,  e imprimir el nombre de la sucursal 
# (Ej. 2 - Garupá)

#Al terminar el ingreso de datos, se pregunta por 
# GRABAR (1) o Cancelar (2). Imprimir el mensaje 
# de error correspondiente si se ha 
# ingresado un valor incorrecto.

import os
def limpiar():
    os.system("cls")

def titulo_subrayado(titulo,caracter="#"):
    print(titulo)
    print(caracter*len(titulo))

def carga(v1,v2,v3,v4,v5):
    archivo=open("persona.txt","r")
    contador=0
    lista=archivo.readline()
    while lista!="":
        contador=contador+1
        lista=archivo.readline()
    archivo.close
    archivo=open("persona.txt","a")
    for x in range(contador):
        contador=contador+1
        archivo.write(str(contador))
        archivo.write(",")
        archivo.write(v2[x])
        archivo.write(",")
        archivo.write(v3[x])
        archivo.write(",")
        archivo.write(v4[x])
        archivo.write(",")
        archivo.write(v5[x])
        archivo.write("\n")
    archivo.close

def continua_nocontinua():
    clave=0
    while clave=="0":
        try:
            clave=int(input("Ingrese la clave del personal: "))
            if clave==0:
                print("fin de la carga")
                limpiar()
                break
            if clave!=0:
                archivo=open("persona.dat","a")
                archivo.close
                break
            else:
                print("La clave no es la correcta")
                clave=int(input("Ingrese la clave del personal: "))
        except:
            print("debe ingresar nuevamente la clave")
    limpiar()

#bloque Principal



diccionario={}
codigo=[]
nombreyapellido=[]
tipo=[]
importe=[]
sucursal=[]
cont=0
op=0


while op==1:
    cont=cont+1
    codigo.append(cont)
    nombreyapellido=input("ingrese el nombre y apellido: ")
    tipo=int(input("ingrese \n1=varon o \n2=mujer \nopcion:  "))
    if tipo>2:
        print("El valor es incorrecto, preste mas atencion")
        tipo=int(input("ingrese \n1=varon o \n2=mujer \nopcion:  "))
    if tipo<1:
        print("El valor es incorrecto, preste mas atencion")
        tipo=int(input("ingrese: \n1-varon o\n2-mujer\nopcion:  "))
    op=int(input("si desea continuar ingrese 0, si no 1"))
    importe=int(input("ingrese el valor del importe: "))
    sucursal=int(input("ingrese: \n1-posadas\n2-Garupa\n3-Candelaria\opcion: "))
    if valor4>3:
        print("La opcion no es la correcta, preste mas atencion: ")
        valor4=int(input("ingrese: \n1-posadas\n2-Garupa\n3-Candelaria\opcion: "))
    if valor4<1:
        print("La opcion no es la correcta, preste mas atencion: ")
        valor4=int(input("ingrese: \n1=posadas\n2=Garupa\n3=Candelaria \opcion: "))
    op=int(input("si desea continuar ingrese 0, si no 1")) 
    diccionario[codigo]=(nombreyapellido,tipo,importe,sucursal)
    

