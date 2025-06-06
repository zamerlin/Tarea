#ABM: alta, baja y modificación de Martínez Mauro Gonzalo#
import os
import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# Paso 1: Filtrar las columnas relevantes
diccionario = {"provincia":{"sexo":{"clasificacion":""}}}

abierto=str(open("Covid19Casos.csv","r",encoding="utf8"))
for linea in abierto:
    print(linea)
    


# Paso 4: Mostrar resultados por pantalla
#print("provincia,sexo,clasificacion,cantidad")
#for provincia, sexos in diccionario_final.items():
#    for sexo, clasificaciones in sexos.items():
#        for clasificacion, cantidad in clasificaciones.items():
#            print(f"{provincia},{sexo},{clasificacion},{cantidad}")

print("[Precione una tecla para continuar]")
msvcrt.getch()
clear()