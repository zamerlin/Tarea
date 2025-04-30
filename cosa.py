cursadas = [["matemática","F", 12],["matemática", "M", 14],
            ["Legislación_Escolar", "M", 12],
            ["Pedagogía", "F", 13],
            ["Lógica", "M", 14],
            ["Archivo_Escolar", 'F', 16],
            ["Pedagogía", "M", 17],
            ["ética", "F", 18],
            ["TICS", "F", 19],]
sumf=0 
summ=0 
sumg=0
canf=0
canm=0 
cang=0
for materia, gen, nota in cursadas:
    sumg += nota
    cang += 1
    if gen == ("F"): 
       sumf += nota
       canf += 1
    elif gen == "M":
       summ += nota
       canm += 1
promedio = sumg/cang 
promf= sumf/canf
promm= summ/canm
print("Promedios: ","mujeres ",promf, "\n","hombres ",promm,"\n","general ",promedio)
