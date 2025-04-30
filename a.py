#Parcial1 Martínez Mauro Gonzalo.
a=[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
sfilas=[]
scolumnas=[0]*len(a[0]) 
for fila in a:
    sumaf=0 
    for magia in fila:
        sumaf+=magia
    sfilas.append(sumaf)
for columna in range(len(a[0])):
    sumac=0
    for fila in range(len(a)):
        sumac+=a[fila][columna]
    scolumnas[columna]=sumac
print("Suma de las filas: ", sfilas ," y Suma de las columnas: ",scolumnas)