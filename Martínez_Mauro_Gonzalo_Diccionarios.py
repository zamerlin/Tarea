import os
import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
diccionario={"nombre":"Taro","dni":44777222,"telefono":2764226313,"email":"taro@gmail.com"}
agenda={}
agenda[44777222]=diccionario

while True:
    print("=====Sistema: Agenda de Contactos=====")
    print("[1] - para agregar un contacto\n[2] - para buscar un contacto\n[3] - para modificar un contacto")
    respuesta=str(input("[4] - para eliminar un contacto\n[5] - para mostrar todos los contactos\n[6] - para salir\n"))
    if respuesta == "1":
        try:
            agregarNombre=str(input("=Ingrese un nombre=\n>>>"))
            agregarDNI=int(input("=Ingrese un DNI=\n>>>"))
            agregartelefono=int(input("=Ingrese un numero de telofono=\n>>>"))
            agregarEmail=str(input("=Ingrese un email=\n>>>"))
            if agregarDNI in agenda:
                print("El dni ingresado ya existe, intente de nuevo=")
            else:                
                diccionario={"nombre":agregarNombre, "dni":agregarDNI, "telefono":agregartelefono, "email":agregarEmail}
                agenda[agregarDNI] = diccionario
        except:
            ValueError
            print("=Error intente de nuevo=")
    
    elif respuesta == "2":
        try:
            buscarContacto=int(input("=Ingrese el dni del contacto a buscar=\n>>>"))
            if buscarContacto in agenda:
                print("=Contacto encontrado sus datos son=")
                print(agenda[buscarContacto])
            else:
                print("=El Contacto no existe, intente nuevamente=")
        except:
            ValueError
            print("=Incorrecto, intente de nuevo=")
    elif respuesta == "3":
        try:
            modificarContacto=int(input("=Ingrese el DNI del contacto a modificar=\n>>>"))
            if modificarContacto in agenda:
                print("=Ingrese que quiere modificar=")
                opcion=str(input("[1] para nombre\n[2] para telefono\n[3] para email\n[4] para salir"))
                while True:
                    if opcion == "1":
                        nuevoNombre=str(input("=Ingrese el nuevo nombre=\n>>>"))
                        agenda[modificarContacto]["nombre"]=nuevoNombre
                    elif opcion == "2":
                        nuevoTelefono=int(input("=Ingrese el nuevo telefono=\n>>>"))
                        agenda[modificarContacto]["telefono"]=nuevoTelefono
                    elif opcion == "3":
                        nuevoEmail=str(input("=Ingrese el nuevo email="))
                        agenda[modificarContacto]["email"]=nuevoEmail
                    elif opcion == "4":
                        break 
                    else:
                        print("Error")
            else:
                print("=El contacto pedido no exite, intente de nuevo=")    
        except:
            ValueError
            print("=Incorrecto, intente de nuevo=\n>>>")
    elif respuesta == "4":
        try:
            eliminarContacto=int(input("=Ingrese el DNI del contacto a eliminar=\n>>>"))
            if eliminarContacto in agenda:
                del agenda[eliminarContacto]
                print(f"=Contacto {eliminarContacto} Eliminado=")
            else:
                print("=El contacto dado no existe, intente de nuevo=")    
        except:
            ValueError
            print("=Incorrecto, intente de nuevo=")
    elif respuesta == "5":
        print(agenda)
        
    elif respuesta == "6":
        print("Saliendo del Sistema")
        break
    
    else:
        print("Error ingrese el codigo correcto")
    
    print("[Presione una tecla para continuar]")
    msvcrt.getch()
    clear()