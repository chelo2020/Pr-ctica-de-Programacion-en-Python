def cargar():
    alumnos={}
    for x in range(3):
        dni=int(input("Ingrese el numero de dni:"))
        listamaterias=[]
        continua="s"
        while continua=="s":
            materia=input("Ingrese el nombre de materia que cursa:")
            nota=int(input("Ingrese la nota:"))
            listamaterias.append((materia,nota))
            continua=input("Desea cargar otra materia para dicho alumno [s/n}:")
        alumnos[dni]=listamaterias
    return alumnos


