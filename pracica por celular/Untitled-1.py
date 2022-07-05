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

def titulo_subrayado(titulo,caracteres="x"):
    print(titulo)
    print(caracteres*len(titulo))

def verificar():
    codigo=1
    while codigo=="0":
        codigo=int(input("ingresar el codigo del empleado: "))
        if codigo==0:
            print("FIN DEL PROGRAMA")
            break
        else:
            codigo!=0
            print("Continuar con la carga")
            break
    limpiar()

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

def carga_datos():
    diccionario={}
    continuar=1
    while continuar==1:
        v1=input("ingresar el nombre y apellido: ")
        v2=int(input("ingresar: 1=varon\n 2=mujer\n opcion: "))
        if v2>2:
            print("El numero es incorrecto, preste mas atencion")
        if v2<1:
            print("El numero es incorrecto, preste mas atencion")
        v3=int(input("ingrese un importe"))
        if v3==0:
            print("Numero incorrecto preste mas atencion")
            v3=int(input("ingrese un importe"))
        v4=int(input("ingrese: 1=posadas\n 2=garupa\n 3=candelaria\n opcion:"))
        if v4>3:
            print("ingreso mal el codigo, preste mas atencion")
        if v4<1:
            print("ingreso mal el codigo, preste mas atencion")
        v5=int(input("ingrese: 1=si quiere gravar\n o 2=cancelar\n opcion: "))
        if v5==1:
            print("continuar con la carga:")
        if v5==2:
            print(" Fin de esta  carga ")
        continuar=int(input("ingrese un 0 si quiere finalizar la carga"))
        diccionario[v1]=(v2,v3,v4)
        
    return diccionario


def consulta_sucursal(diccionario):
    v1=input("ingresar el nombre de la sucursal: ")
    for v1 in diccionario:
        print(v1,diccionario[v1][3])

#Bloque Principal
titulo_subrayado("           BIENVENIDOS AL PROGRAMA DE CARGA      ")
diccionario=carga_datos()
consulta_sucursal(diccionario)
titulo_subrayado("    FIN DEL PROGRAMA      ")






