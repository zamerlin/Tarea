# Lista original de datos
datos = [['José', '19-03-1980', 'Ford', 'Ka'],
    ['José', '19-03-1980', 'Ford', 'EcoSport'],
    ['Lucas', '18-10-1992', 'Renault', 'Logan'],
    ['Felipe', '03-05-1995', 'Ford', 'Mondeo'],
    ['Felipe', '03-05-1995', 'Honda', 'Civic'],
    ['María', '08-09-1980', 'Fiat', 'Doblo'],
    ['Lucas', '18-10-1992', 'Renault', 'Sandeo'],
    ['José', '19-03-1980', 'Fiat', 'Fiorino'],
    ['Pedro', '29-06-1986', 'Nissan', 'Pathfinder'],
    ['Santiago', '25-07-1985', 'Jeep', 'Renegade'],
    ['Felipe', '03-05-1995', 'Hyundai', 'Santa Fe'],
    ['María', '08-09-1980', 'Fiat', '600'],
    ['Andrés', '30-11-1989']]

# Crear un diccionario para almacenar la información
personas = {}

# Recorrer la lista de datos
for item in datos:
    nombre = item[0]
    fecha = item[1]
    auto = item[2:]  # El auto está en la posición 2 en adelante
    
    # Si la persona ya está en el diccionario, agregar el auto
    if nombre in personas:
        personas[nombre]['autos'].append(auto)
    else:
        # Si no está, agregar una nueva entrada
        personas[nombre] = {'fecha': fecha, 'autos': [auto]}

# Convertir el diccionario en la lista de listas
resultado = [[nombre, data['fecha'], data['autos']] for nombre, data in personas.items()]

# Imprimir el resultado
print(resultado)
