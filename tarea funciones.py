#tarea funciones#
def relacion(a,b):
    if a>b:
        print("1")
    elif a<b:
        print("-1")
    elif a==b:
        print("0")

try:
    numero1=int(input("introdusca un número\n>>>"))
    numero2=int(input("introdusca un segundo número\n>>>"))
    relacion(numero1,numero2)

except:
    ValueError
    print("ingrese un numero entero")