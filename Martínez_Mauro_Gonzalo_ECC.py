#clase3: ingresar nota, nota de esfuerzo y devuelve palabras calificativas por Martínez Mauro Gonzalo#
print("Ingrese una nota numerica, una en base al esfuerzo y obtenga una nota personalizada")

while True:
    notaNumerica=input("Ingrese la nota del estudiante: de 0 a 100\n ")
    if notaNumerica.isdigit():    
        if notaNumerica >= 0 and notaNumerica <=100:
            print("Nota numerica correcta") 
            break
        else:
            print("Nota numerica incorrecta, intente de nuevo")
    else:
        print("Ingrese un numero")
        
while True:
    notaEsfuerzo=str(input("Ingrese la nota de esfuerzo del estudiante: (B) para Baja, (M) par Media y (A) para Alta\n"))
    notaEsfuerzo=notaEsfuerzo.upper()
    if notaEsfuerzo == "A" or notaEsfuerzo == "M" or notaEsfuerzo == "B":
        print("Nota de esfuerzo correcta")
        break
    else:
        print("Nota de esfuerzo incorrecta intente de nuevo")

nota=""
if notaNumerica >= 0 and notaNumerica <= 49:
    nota="Reprobado"
elif notaNumerica >= 50 and notaNumerica <= 69:
    nota="Necesita mejorar"
elif notaNumerica >= 70 and notaNumerica <= 89:
    nota="Aprobado"
elif notaNumerica >= 90 and notaNumerica <=100:
    nota="Sobresaliente"

notaEsf=""
if notaEsfuerzo == "B":
    if notaNumerica >= 0 and notaNumerica <= 49: 
        notaEsf=", tendrias que ponerle mucho más esfuerzo para mejorar tu nota"
    elif notaNumerica >= 50 and notaNumerica <= 69:
        notaEsf=", con más esfuerzo la proxima seguro llegaras más lejos"
    elif notaNumerica >= 70 and notaNumerica <= 89:
        notaEsf=", seguro que si te esforzaras más sacabas mayor nota"
    elif notaNumerica >= 90 and notaNumerica <=100:
        notaEsf=", talvez si te esforzaras disfrutarias más de aprender"

elif notaEsfuerzo == "M":
    if notaNumerica >= 0 and notaNumerica <= 69:
        notaEsf=", deberias ponerle más ganas para aumentar tu nota"
    elif notaNumerica >= 70 and notaNumerica <= 100:
        notaEsf= ", buen trabajo pero tendrias que ponerle más esfuerzo"

elif notaEsfuerzo == "A":
    if notaNumerica >= 0 and notaNumerica <= 49: 
        notaEsf=", se valora tu esfuerzo seguramente la proxima lo logras si te esfuerzas más"
    elif notaNumerica >= 50 and notaNumerica <= 69:
        notaEsf=", se valora tu esfuerzo seguro que con más esfuerzo podrias mejorar"
    elif notaNumerica >= 70 and notaNumerica <= 89:
        notaEsf=", se valora tu esfuerzo !Buen Trabajo¡"
    elif notaNumerica >= 90 and notaNumerica <=100:
        notaEsf=", se valora tu esfuerzo !increible¡"

print(nota, notaEsf)