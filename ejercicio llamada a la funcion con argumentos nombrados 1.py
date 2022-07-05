# confeccionar una funcion que reciba de un operario,
#el pago pro hora y la cantidad de horas trabajadas.
# debe mostrar su sueldo y el nombre. Hacer la llamada 
# de la funcion mediante  argumentos nombrados.

def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras," y cobra un sueldo de",sueldo)

# bloque principal

calcular_sueldo("juan",10,120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="marcelo")
calcular_sueldo(cantidadhoras=56,nombre="mirta",costohora=10)
