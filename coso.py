#lista de martínez mauro#
lista= []

numeroPersonas=int(input("ingrese un numero de personas a añadir a la lista : "))

for i in range(numeroPersonas):
    lista.append(input(f"ingresa a la {i + 1} persona a agregar a la lista : "))
    
print(lista)

eliminar=(input("ingrese el nombre a eliminar: "))

lista.remove(eliminar)

print(eliminar," fue eliminado")
print(lista)

numeroEliminar=int(input(f"ingrese un numero de la lista para eliminar a partir 1 hasta {len(lista)}: "))

lista.pop(numeroEliminar-1)

print(numeroEliminar,"fue eliminado")
print(lista)