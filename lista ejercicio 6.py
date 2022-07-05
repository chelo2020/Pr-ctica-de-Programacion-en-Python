nombres=["juan","marcelo","analia","marcos","sebastian"]
x=0
suma=0

for x in range(len(nombres)):
    if len(nombres[x])>=5:
        suma=suma+1

print("los nombres con mas de 5 caracteres son:")
print(suma)

        