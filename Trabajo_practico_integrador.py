#Trabajo Practico integrador por Gonzalez Adrian y Martínez Mauro.
import sqlite3
import os
import msvcrt
from Trabajo_practico_integradorBD import *

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
conexion = sqlite3.connect('Churrito el capibara.db') 
conexion.execute("PRAGMA foreign_keys = ON;")
# Intreracciones y Llamadas de Funciones
cID = 1
while True:
    try:
        clear()
        print("=Menu de Selección=")
        eleccion = str(input("[1]Modulo de Venta\n[2]Modulo de Administración\n[3]Salir del Sistema\n>>> "))
        clear()
        if eleccion == "1":
            
            while True:
                print("=Menu de Seleccion del Modulo Venta=")
                respuesta = str(input("[1]Venta por pedido\n[2]Venta en Local\n[3]Volver al Menu Anterior\n>>> "))
                if respuesta == "1":
                    clear()
                    pedid = str(input("=Ingrese la opción=\n[1] Realizar un pedido\n[2] Realizar la venta de un pedido\n>>> "))
                    if pedid == "1":
                        clear()
                        cID = listarClientes(cID)
                        #print(f" despues de la funcion {cID}")
                        if cID == 0:
                            print(cID)
                            break
                        else:
                            clienteID = int(input("=Ingrese el numero del cliente para realizar el pedido=\n>>> "))
                            if cID == 0:
                                print(cID)
                                break
                            listarChurros()
                            churroID = int(input("=Ingrese el numero del churro para realizar el pedido=\n>>> "))
                            pedidos(clienteID, churroID)
                            #funcion de Venta x Pedido
                    elif pedid == "2":
                            cursor = conexion.cursor()
                            cursor.execute("SELECT * FROM Pedidos")
                            pedidos = cursor.fetchall()
                            if not pedidos:
                            #Verifica si hay clientes registrados
                                clear()
                                print("=No hay Pedidos registrados=")
                                print("=Ingrese una tecla para continuar=")
                                msvcrt.getch()
                            else:
                                listarPedidos()
                                pedidoID = int(input("=Ingrese el numero del pedido para concretar la venta=\n>>> "))
                                VentaDelPedido(pedidoID)
                    else:
                        print("=Opción inválida=")
                elif respuesta == "2":
                    clear()
                    listarChurros()
                    Estado = "Activo"
                    cursor = conexion.cursor()
                    cursor.execute("SELECT * FROM Churros Where Estado = ?", (Estado,))
                    churros = cursor.fetchall()
                    if not churros:
                        break
                    churroID = int(input("=Ingrese el numero del churro solicitado=\n>>> "))
                    RegistrarVentaUnidad(churroID)
                    #funcion de Venta Presencial/ x ventanilla/ en Local
                elif respuesta == "3":
                    clear()
                    print("=Volviendo al Menu anterior=") 
                    break 
                else:
                    clear()
                    print("=Incorrecto Intente de Nuevo=")
                    print("[Presione una tecla para continuar]")
                    msvcrt.getch()
                clear()
        elif eleccion == "2":
            while True:
                clear()
                print(f"=Menu de Administración=")
                print("[1]Agregar\n[2]Modificar\n[3]Ver registro de Pedidos")
                print("[4]Ver registro de Ventas de los pedidos\n[5]Ver registro de ventas por ventana")
                administracion = str(input("[6]Para descargar los Registros de las Ventas \n[7]Volver al Menu Anterior\n>>> "))
                if administracion == "1":
                    clear()
                    opc = str(input("=Ingrese la opcion a agregar=\n[1] Producto\n[2] Cliente\n[3] Volver\n>>> "))
                    #funcion de agregar un producto
                    if opc == "1":
                        NuevoChurro()
                    elif opc == "2":
                        CrearCliente()
                    elif opc == "3":
                        print("=Volviendo=")
                        print("[Presione una tecla para continuar]")
                        msvcrt.getch()
                        break
                    else:
                        clear()
                        ("=Opción inválida, volviendo=")
                        print("[Presione una tecla para continuar]")
                        msvcrt.getch()
                                    
                elif administracion == "2":
                    clear()
                    opc = str(input("=Seleccione la opción a modificar=\n[1] Modificar un producto\n[2] Modificar un cliente\n[3] Volver\n>>> "))
                    #funcion de modificar X cosa
                    if opc == "1":
                        modificarChurros()
                        clear()    
                        #print("=Modificado, Volviendo al Menu Anterior=")
                        #funcion modificar productos
                    elif opc == "2":
                        modificarCliente()
                        clear()    
                        #print("=Modificado, Volviendo al Menu Anterior=")
                        #funcion modificar clientes
                    elif opc == "3":
                        print("=Volviendo=")
                        print("=Presione una tecla para continuar=")
                        msvcrt.getch()
                    else:
                        print("=Opción inválida, volviendo al menu anterior=")
                        print("[Presione una tecla para continuar]")
                        msvcrt.getch()
                elif administracion == "3":
                    clear()
                    listarPedidos()
                elif administracion == "4":
                    clear()
                    listarVentasPP()
                elif administracion == "5":
                    clear()
                    listarVentasPV()
                elif administracion == "6":
                    clear()
                    print("=Descargando las ventas=")
                    registroVenta()
                    registroVentana()
                elif administracion == "7":
                    clear()    
                    print("=Volviendo al Menu Anterior=")
                    print("[Presione una tecla para continuar]")
                    msvcrt.getch()
                    break
                else:
                    clear()
                    print("Opción no válido")
                    print("[Presione una tecla para continuar]")
                    msvcrt.getch()
        elif eleccion == "3":
            clear()
            conexion.close()
            exit("=Saliendo! Tenga un bonito descanso [^-^)/]=")
        else:
            clear()
            print("=Incorrecto, Intente de Nuevo=")
            print("[Presione una tecla para continuar]")
            msvcrt.getch()
    except ValueError:
        clear()
        print("=Error, ingrese un valor correcto en donde se le solicita=")
        print("[Presione una tecla para continuar]")
        msvcrt.getch()