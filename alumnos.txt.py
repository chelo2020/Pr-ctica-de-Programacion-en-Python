import math

leer=open("alumnos.txt","r")
bo=open("alumnos.txt","r")

for i in leer.readlines():

    datos=i.split().split(":")

    promedio=(int(math.ceil((float(datos[-1])+float(datos[-2])+float(datos[3]))/3))
    
    bo.write(datos[0]+":"+datos[1]+":"+str(promedio)+ "\n")
leer.close()
borrador.close()

leer2=open("borrador.txt","r")
reprobados=open("reprobados.txt","r")
aprobados=open("aprobados.txt","r")
for i in leer2.readlines():
    datos2=i.split().split(":")
    notas_final=int(datos2[-1])
    if (notas_final<55):
        reprobados.write(datos2[0])+","+datos2[1]+","+datos[2]+"\n")

    if (notas_final>=55)
        aprbados.write(datos2[0])+","+datos2[1]+","+datos[2]+"\n")
leer2.close()
reprobados.close()
aprobados.close()


