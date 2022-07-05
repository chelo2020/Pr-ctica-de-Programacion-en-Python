x=0
p_cuadrante=0
s_cuadrante=0
t_cuadrante=0
c_cuadrante=0
f=0
y=0
puntos=int(input("ingrese la cantidad de puntos a estudia: "))

for f in range(puntos):
    x=int(input("ingrese el punto correspondiente a x: "))
    y=int(input("ingrese el punto correspondiente a y: "))
    if x>0 and y>0:
        p_cuadrante=p_cuadrante+1
    else:
        if x<0 and y>0:
            s_cuadrante=s_cuadrante+1
        else:
            if x<0 and y<0:
                t_cuadrante=t_cuadrante+1
            else:
                if x>0 and y<0:
                    c_cuadrante=c_cuadrante+1


print("los puntos pertenecientes al primer cuadrante es: ")    
print(p_cuadrante)
print("los puntos pertenecientes al segundo cuadrante es: ")
print(s_cuadrante)
print("los puntos pertenecientes al tercer cuadrante es: ")
print(t_cuadrante)
print("los puntos pertenecientes al cuarto cuadrante es: ")
print(c_cuadrante)


