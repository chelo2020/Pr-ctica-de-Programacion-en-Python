def cargar():
    agenda={}
    continua1="s"
    while continua1=="s":
        fecha=input("ingrese la fecha con formato dd/mm/aa:")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=input("Ingrese la hora de la actividad con formato hh:mm ")
            actividad=input("Ingrese la descripcon de la actividad:")
            lista.append((hora,actividad))
            continua2=input("Ingresa otra actividad para la misma fecha[s/n]:")
        agenda[fecha]=lista
        continua1=input("Ingresa otra fecha[s/n]:")
    return agenda       


def imprimir(agenda):
    print("imprimir la agenda completa")
    for fecha in agenda:
        print("para la fecha",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)

def consulta_fecha(agenda):
    fecha=input("ingrese la fecha")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("no hay fecha para dicha actividad")

# Bloque principal

agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)

