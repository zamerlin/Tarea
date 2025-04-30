#ABM: alta, baja y modificación de Martínez Mauro Gonzalo#
import os
import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
listaABM=[["loto@email.com","pepelgrillo"],["mate@email.com","matedelosdioses"],["pepino@email.com","ensaldadepepino"]]
    
while True:
    
    print("====Bienvenido al sistema====")
    comando=str(input(" ====Ingrese un comando====\n [1] para agregar un usuario\n [2] para eliminar un usuario\n [3] para modificar un usuario\n [4] para mostrar la lista entera de usuarios\n [5] para salir\n>>>"))
    comando=comando.upper()

    if comando == "1":

        agregar=[]
        
        print("=Bienvenido a agregar un usuario al sistema=\n=Ahora se le pedira un email y una contraseña para el usuario a agregar=")
        agregarCorreo=str(input("=Ingrese el Correo Electronico=\n>>>"))
        agregarContraseña=str(input("=Ingrese la Contraseña=\n>>>"))
        
        agregar.append(agregarCorreo+"@email.com")
        agregar.append(agregarContraseña)
        
        listaABM.append(agregar)
        print("=Usuario creado exitosamente=\n",agregar)
            
    elif comando == "2":
        
        print("=Bienvenido a eliminar un usuario del sistema=")
        for contador in range(len(listaABM)):
             print("ID ",contador+1,listaABM[contador][0])
        while True:
            
            try:

                eliminarUsuario=int(input("=Ingrese el ID del usuario a eliminar=\n>>>"))
                if eliminarUsuario <= contador+1:
                    
                    print("se selecciono",listaABM[eliminarUsuario-1], "para ser eliminado")
                    listaABM.pop(eliminarUsuario-1)
                    for contador in range(len(listaABM)):
                        print("ID ",contador+1,listaABM[contador][0])
                    print("=El usuario ID ", eliminarUsuario, "fue eliminado correctamente=")
                    break
                elif eliminarUsuario <= 0:
                
                    print("=error ingrese un ID correcto=")
                else:
                
                    print("=error ingrese un ID correcto=")
            except:
                ValueError
                print("=error ingrese un ID correcto=")
            
    elif comando == "3":
        
        print("=Bienvenido a modificar un usuario del sistema=")
        for contador in range(len(listaABM)):
        
            print("ID ",contador+1,listaABM[contador][0])
        while True:
            
            try:
               
                modificarUsuario=int(input("=Ingrese el ID del usuario a eliminar=\n>>>"))
                if modificarUsuario <= contador+1:
                    
                    listaModificar=[]
                    listaABM.pop(modificarUsuario-1)
                    
                    agregarCorreo=str(input("=Ingrese el nuevo Correo Electronico=\n>>>"))
                    agregarContraseña=str(input("=Ingrese la nueva Contraseña=\n>>>"))
                    
                    listaModificar.append(agregarCorreo+"@email.com")
                    listaModificar.append(agregarContraseña)
                    
                    listaABM.insert(modificarUsuario-1,listaModificar)
                    for contador in range(len(listaABM)):
                        print("ID ",contador+1,listaABM[contador][0])
                    print("=El usuario ID ", modificarUsuario, "fue modificado exitosamente=\n",listaModificar)
                    
                    break
                
                elif modificarUsuario <= 0:
                
                    print("=error ingrese un ID correcto=")
                else:
                
                    print("=error ingrese un ID correcto=")
            except:
                
                ValueError
                print("=error ingrese un ID correcto=")

    elif comando == "4":
        
        print("=Bienvenido esta es la lista de usuarios=")
        contador=0
        while True:
            
            print(f"Usuario {contador+1}\n[",listaABM[contador][0],"]")
            contador+=1
            if contador == len(listaABM):
                
                break
            
    elif comando == "5":
        
        print("=Saliendo del sistema=")
        break
    
    else:
        
        print("=Comando incorrecto, intente de nuevo=")
        
    print("[Precione una tecla para continuar]")
    msvcrt.getch()
    clear()