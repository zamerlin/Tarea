#Trabajo Practico integrador por Gonzalez Adrian y Martínez Mauro.
import sqlite3
import msvcrt
import os
conexion = sqlite3.connect('Churrito el capibara.db') 
conexion.execute("PRAGMA foreign_keys = ON;")
from datetime import datetime
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

print("=Bienvenido al sistema=\n")
#----------------------------------------Crear la tabla de Clientes---------------------------------
conexion.execute("""create table if not exists Clientes
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 DNI INTEGER NOT NULL,
                 Apellido TEXT NOT NULL,
                 Nombre TEXT NOT NULL,
                 Telefono INTEGER NOT NULL,
                 Negocio TEXT NOT NULL,
                 Estado TEXT NOT NULL
                 );""")
conexion.commit()
#-------------------------------Crear la tabla de tipos y precio de los Churros:---------------------------------
conexion.execute("""create table if not exists Churros
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 PRODUCTO TEXT NOT NULL,
                 PrecioDoc INTEGER NOT NULL,
                 PrecioUni INTEGER NOT NULL,
                 Estado TEXT NOT NULL
                 );""")
conexion.commit()
#----------------------------------------Crear la tabla de Pedidos:---------------------------------
conexion.execute("""create table if not exists Pedidos
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Cantidad INTEGER NOT NULL,
                 Fecha TEXT NOT NULL,
                 ID_Clientes INTEGER NOT NULL,
                 ID_Churros INTEGER NOT NULL,
                 Total INTEGER NOT NULL,
                 FOREIGN KEY (ID_Clientes) REFERENCES Clientes(ID),
                 FOREIGN KEY (ID_Churros) REFERENCES Churros(ID)
                 );""")
conexion.commit()
#----------------------------------------Crear la tabla de Ventas por pedido:---------------------------------
conexion.execute("""create table if not exists VentasPP
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 ID_Churros INTEGER NOT NULL,
                 Precio INTEGER NOT NULL,
                 Fecha TEXT NOT NULL,
                 ID_Clientes INTEGER NOT NULL,
                 ID_Pedidos INTEGER NOT NULL,
                 FOREIGN KEY (ID_Clientes) REFERENCES Clientes(ID),
                 FOREIGN KEY (ID_Pedidos) REFERENCES Pedidos(ID),
                 FOREIGN KEY (ID_Churros) REFERENCES Churros(ID));""")
conexion.commit()
#----------------------------------------Crear la tabla de Ventas por Ventana:---------------------------------
conexion.execute("""create table if not exists VentasPV
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 ID_Churros INTEGER NOT NULL,
                 Cantidad INTEGER NOT NULL,
                 Precio INTEGER NOT NULL,
                 Total INTEGER NOT NULL,
                 Fecha TEXT NOT NULL,
                 FOREIGN KEY (ID_Churros) REFERENCES Churros(ID));""")
conexion.commit()
#--------------------------------------Crea un cliente----------------------------
def CrearCliente():
    try:
        dni = 0
        while dni < 10000000 or dni > 99999999:
            clear()
            dni = int(input("=Ingrese el número de su DNI sin puntos ni comas=\n>>> "))
            if dni < 10000000 or dni > 99999999:
                clear()
                print("=Error, El DNI debe tener 8 números=")
                print("[Presione una tecla para continuar]")
                msvcrt.getch()
        cursor = conexion.cursor()
        cursor.execute("SELECT DNI FROM Clientes WHERE DNI = ?", (dni,))
        if cursor.fetchone():
            #Verifica si el cliente ya existe
            clear()
            print(f"=Este DNI ({dni}) ya existe=")
            print("[Presione una tecla para continuar]")
            msvcrt.getch()
            return
        #si no existe
        Apellido = str(input("=Ingrese el/los Apellido/s del cliente=\n>>> ")).capitalize()
        Nombre = str(input("=Ingrese el nombre completo del cliente=\n>>> ")).capitalize()
        Telefono = int(input("=Ingrese su número de teléfono del cliente=\n>>> "))
        Negocio = str(input("=Ingrese la institución y/o negocio del cliente=\n>>> ")).capitalize()
        Estado = "Activo"
        #Conectar con los datos:
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO Clientes(DNI, Apellido, Nombre, Telefono, Negocio, Estado) 
                       VALUES (?, ?, ?, ?, ?, ?)""",
                    (dni, Apellido, Nombre, Telefono, Negocio, Estado))
        conexion.commit()
        clear()
        print("=Cliente agendado con exitosamente=")
        print("[Presione una tecla para continuar]")
        msvcrt.getch()

    except ValueError:
        clear()
        print("=Error, Ingrese un valor adecuado=\n=El sistema se reiniciará=")
        print("[Presione una tecla para continuar]")
        msvcrt.getch()
#---------------------------------------mostrar los clientes al buscar y detectar------------------------------
def listarClientes(clienteID):
    clear()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Clientes")
    Clientes = cursor.fetchall()
    cursor.execute("SELECT * FROM Clientes WHERE ID = ?", (clienteID,))
    clientes = cursor.fetchall()
    for cliente in clientes:
        if clienteID not in cliente:
            a = 0
            print(f"=El cliente N° {clienteID} no existe=")
            return a
    if not Clientes:
        a = 0
        print(a)
        #Verifica si hay clientes registrados
        print("=No hay Clientes registrados=")
        print("[Presione una tecla para continuar]")
        msvcrt.getch()
        return a
    else:
        a = 1
        for Cliente in Clientes:
            print(f"Cliente N°: {Cliente[0]}\nDNI: {Cliente[1]}\nApellido: {Cliente[2]}\nNombre: {Cliente[3]}\nTel: {Cliente[4]}\nNegocio: {Cliente[5]}")
            print(" ")
        return a

#---------------------------------------mostrar los clientes comun------------------------------
def listarClientesuno():
    clear()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Clientes")
    Clientes = cursor.fetchall()
    for Cliente in Clientes:
        print(f"Cliente N°: {Cliente[0]}\nDNI: {Cliente[1]}\nApellido: {Cliente[2]}\nNombre: {Cliente[3]}\nTel: {Cliente[4]}\nNegocio: {Cliente[5]}")
        print(" ")
#------------------------------------------------Modifica el Cliente------------------------
def modificarCliente():
    try:
        Estado = "Activo"
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Clientes Where Estado = ?", (Estado,))
        clientes = cursor.fetchall()
        if not clientes:
            #Verifica si hay churros registrados
            print("=No hay clientes registrados, ¿Desea registrar a uno?=")
            opc = int(input("[1] Si [2] No\n>>> "))
            if opc == 1:
                CrearCliente()
            elif opc == 2:
                print("=Volviendo al menú principal=")
                print("=Ingrese una tecla para continuar=")
                msvcrt.getch()
                return
            else:
                print("=Opción inválida, Volviendo al menú principal=")
                print("=Ingrese una tecla para continuar=")
                msvcrt.getch()
                return
        else:
            listarClientesuno()
            DNI = str(input("=Ingrese el DNI del Cliente que desea modificar=\n>>> "))
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Clientes WHERE DNI = ?", (DNI,))
            cliente = cursor.fetchone()

            if not cliente:
                print(f"=El cliente {DNI} no existe ¿Desea crearlo?=")
                opc = int(input("[1] Si\n[2] No\n>>> "))
                if opc == 1:
                    CrearCliente()
                elif opc == 2:
                    print("=Volviendo al menú principal=")
                    print("[Presione una tecla para continuar]")
                    msvcrt.getch()
                    return
                else:
                    print("=Opción inválida, Volviendo al menú principal=")
                    print("[Presione una tecla para continuar]")
                    msvcrt.getch()
                    return
            else:
                nombre = str(input("=Ingrese su nuevo nombre=\n>>> ")).capitalize() 
                apellido = str(input("=Ingrese su nuevo apellido=\n>>> ")).capitalize()
                telefono = int(input("=Ingrese su nuevo teléfono=\n>>> "))
                negocio = str(input("=Ingrese el nuevo nombre del negocio=\n>>> ")).capitalize()
                estado = ""
                while estado not in ["Activo", "Inactivo"]:
                    estado = str(input("=Ingrese el estado en que se encuentre el cliente (Activo o Inactivo)=\n>>> ")).capitalize()
                
                # Actualiza los datos
                cursor.execute("""
                    UPDATE Clientes 
                    SET Apellido = ?, Nombre = ?, Telefono = ?, Negocio = ?, Estado = ?
                    WHERE DNI = ?
                """, (apellido, nombre, telefono, negocio, estado, DNI))
                conexion.commit()

                print("=Cliente modificado exitosamente=")
                print("[Presione una tecla para continuar]")
                msvcrt.getch()
    except TypeError:
        print("=No deje campos vacíos=")
        print("[Presione una tecla para continuar]")
        msvcrt.getch()

        
#---------------------------------------------Ingresa un tipo de Churro-------------------------------
def NuevoChurro():
    cursor = conexion.cursor()
    try:
        nuevo = str(input("=Ingrese el nombre del nuevo tipo de churro=\n>>> ")).capitalize()
        cursor = conexion.cursor()
        cursor.execute("SELECT Producto FROM Churros WHERE Producto = ?", (nuevo,))
        if cursor.fetchone():
            #Verifica si el Producto ya existe
            clear()
            print(f"=El producto ({nuevo}) ya existe=")
            print("[Presione una tecla para volver]")
            msvcrt.getch()
            return
        precioDoc = int(input(f"=Ingrese el precio por docena del Producto {nuevo}=\n>>> "))
        precioUni = int(input(f"=Ingrese el precio por unidad del Producto {nuevo}=\n>>> "))
        Estado = "Activo"
        cursor.execute("""
            INSERT INTO Churros(Producto, PrecioDoc, PrecioUni, Estado) VALUES (?, ?, ?, ?)""",
            (nuevo, precioDoc, precioUni, Estado))
        print("=Nuevo producto Agregado=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
        Estado = "Activo"
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Churros Where Estado = ?", (Estado,))
        chrros = cursor.fetchall()
        for churro in chrros:
            print(f"Numero [{churro[0]}] Producto: {churro[1]}\nPrecio por docena: {churro[2]}\nPrecio por unidad: {churro[3]}\nEstado del producto: {churro[4]}")
            print(" ")
    except ValueError:
        print("=Error, Ingrese datos adecuadamente donde se solicite=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
        return
    conexion.commit()
#--------------------------------------------------Listar Churros------------------------------
def listarChurros():
    Estado = "Activo"
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Churros Where Estado = ?", (Estado,))
    chrros = cursor.fetchall()
    if not chrros:
        #Verifica si hay churros registrados
        print("=No hay productos registrados, ¿Desea crear uno?=")
        try:
            opc = int(input("[1] Si [2] No\n>>> "))
            if opc == 1:
                NuevoChurro()
            elif opc == 2:
                print("=Volviendo al menú principal=")
                print("=Ingrese una tecla para continuar=")
                msvcrt.getch()
                return
            else:
                print("=Opción inválida, Volviendo al menú principal=")
                print("=Ingrese una tecla para continuar=")
                msvcrt.getch()
                return
        except ValueError:
            print("=Error, Ingrese los datos correctos donde se le solicita=")
            print("=Ingrese una tecla para continuar=")
            msvcrt.getch()
    else:
        for churro in chrros:
            print(f"Numero [{churro[0]}] Producto: {churro[1]}\nPrecio por docena: {churro[2]}\nPrecio por unidad: {churro[3]}\nEstado del producto: {churro[4]}")
            print(" ")

#------------------------------------------------Modifica el Producto------------------------
def modificarChurros():
    try:
        Estado = "Activo"
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Churros Where Estado = ?", (Estado,))
        chrros = cursor.fetchall()
        if not chrros:
            #Verifica si hay churros registrados
            print("=No hay productos registrados, ¿Desea crear uno?=")
            opc = int(input("[1] Si [2] No\n>>> "))
            if opc == 1:
                NuevoChurro()
            elif opc == 2:
                print("=Volviendo al menú principal=")
                print("=Ingrese una tecla para continuar=")
                msvcrt.getch()
                return
            else:
                print("=Opción inválida, Volviendo al menú principal=")
                print("=Ingrese una tecla para continuar=")
                msvcrt.getch()
                return
        else:
            listarChurros()
            Chrro = str(input("=Ingrese numero del Producto que desea modificar=\n>>> "))
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Churros WHERE ID = ?", (Chrro,))
            Churros = cursor.fetchone()
            if not Churros:
                #verifica si está el cliente
                print(f"=El producto {Chrro} no está registrado, ¿Desea crearlo?=")
                opc = int(input("[1] Si [2] No\n>>> "))
                if opc == 1:
                    NuevoChurro()
                elif opc == 2:
                    clear()
                    print("=Volviendo al menú principal=")
                    print("=Ingrese una tecla para continuar=")
                    msvcrt.getch()
                    return
                else:
                    clear()
                    print("=Opción inválida, Volviendo al menú principal=")
                    print("=Ingrese una tecla para continuar=")
                    msvcrt.getch()
                    return
            else:
                clear()
                print("=Producto encontrado=")
                print(Churros)
                print(Churros[0])
                uno = Churros[2]
                dos = Churros[3]
                print(uno)
                print(dos)
                NuevoChrr = str(input("=Ingrese el nuevo nombre del Producto o presione enter para no modificar=\n>>> ")).capitalize() or Churros[1]
                print(NuevoChrr)
                precioDoc = int(input(f"=Ingrese el nuevo precio por docena del Producto o presione enter para no modificar=\n>>> ")) or uno
                print(precioDoc)
                precioUni = int(input(f"=Ingrese el nuevo precio por unidad del Producto o presione enter para no modificar=\n>>> ")) or dos
                print(precioUni)
                while Estado != "Activo" or Estado != "Inactivo":
                    Estado = str(input("=Ingrese el nuevo estado del Producto (Activo - Inactivo) o presione enter para no modificar=\n>>> ")).capitalize() or Churros[4]
                    if Estado != "Activo" or Estado != "Inactivo":
                        clear()
                        print("=Error, El estado solo puede ser Activo o Inactivo=")
                        print("=Presione una tecla para continuar=")
                        msvcrt.getch()
                #Actualiza los datos
                cursor.execute("""
                    UPDATE Churros SET Producto = ? PrecioDoc = ? PrecioUni= ? Estado = ?
                    WHERE Chrro = ?
                    """,(NuevoChrr, precioDoc, precioUni, Estado))
                conexion.commit()
                clear()
                print("=Producto Modificado con éxito=")
                print("=Presione una tecla para continuar=")
                msvcrt.getch()
    except ValueError:
        clear()
        print("=Error, Ingrese un valor numérico=\n=El sistema se reiniciará=")
        print("=Presione una tecla para continuar=")
        msvcrt.getch()
#-----------------------------------------Crear un pedido--------------------------
def pedidos(clienteID, churroID):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Churros WHERE ID = ?", (churroID,))
        churros = cursor.fetchall()
        for churro in churros:
            if churroID not in churro:
                #print("=No hay pedidos=")
                break
            else:
                cantidad = int(input("=Ingrese la cantidad por docena=\n>>> "))
                precio = churros[0]
                pcio = precio[2]
                total = cantidad * pcio
                fecha_actual = datetime.now()
                cursor.execute("""
                        INSERT INTO Pedidos(Cantidad, Fecha, ID_Clientes, ID_Churros, Total) VALUES (?, ?, ?, ?, ?)""",
                        (cantidad, fecha_actual, clienteID, churroID, total))
                print("=Nuevo Pedido agregado=")
                conexion.commit()
                return
        print(f"=El producto N° {churroID} no se encuentra inscripto=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
    except sqlite3.Error as e:
        print(f"=Error al realizar el pedido, Usuario inexistente=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
    except ValueError:
        print("=Error, Volviendo al sistema=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
#----------------------------------------Listar pedidos------------------------------------
def listarPedidos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Pedidos")
    pedidos = cursor.fetchall()
    if not pedidos:
        #Verifica si hay pedidos registrados
        print("=No hay Pedidos registrados=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
        return
    else:
        for pedido in pedidos:
            clear()
            print(f"Número del pedido: {pedido[0]}\nCantidad: {pedido[1]}\nFecha {pedido[2]}\nID Cliente: {pedido[3]}\nID Churro: {pedido[4]}\nTotal: {pedido[5]}")
            print(" ")
            print("=Ingrese una tecla para continuar=")
            msvcrt.getch()
#----------------------------------------Listar ventas Por pedidos------------------------------------
def listarVentasPP():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM VentasPP")
    ventas = cursor.fetchall()
    if not ventas:
        #Verifica si hay pedidos registrados
        print("=No hay ventas registradas=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
        return
    else:
        for venta in ventas:
            print(f"Número de venta: {venta[0]}\nProducto: {venta[1]}\nTotal {venta[2]}\nFecha: {venta[3]}\nCliente: {venta[4]}\nPedido N°: {venta[5]}")
            print(" ")
            print("=Ingrese una tecla para continuar=")
            msvcrt.getch()
#----------------------------------------Listar ventas Por ventana------------------------------------
def listarVentasPV():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM VentasPV")
    ventas = cursor.fetchall()
    if not ventas:
        #Verifica si hay pedidos registrados
        print("=No hay ventas registradas aún=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
        return
    else:
        for venta in ventas:
            print(f"Número de venta: {venta[0]}\nProducto: {venta[1]}\nCantidad {venta[2]}\nPrecio: {venta[3]}\nTotal: {venta[4]}\nFecha: {venta[5]}")
            print(" ")
            print("=Ingrese una tecla para continuar=")
            msvcrt.getch()

#------------------------------------Registrar una venta por unidad-------------------------
def RegistrarVentaUnidad(churroID):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Churros WHERE ID = ?", (churroID,))
        churro = cursor.fetchall()
        if not churro:
            print("=La opción seleccionada no esta disponible=")
            print("[Presione una tecla para continuar]")
            msvcrt.getch()
        else:
            cantidad = int(input("=Ingrese la cantidad de churros=\n>>> "))
            total = cantidad * churro[0][3]
            fecha_actual = datetime.now()
            cursor.execute("""
                INSERT INTO VentasPV(ID_Churros, Cantidad, Precio, Total, Fecha) VALUES (?, ?, ?, ?, ?)""",
                (churroID, cantidad, churro[0][3], total, fecha_actual))
            print("=Venta completada con éxito=")
            print(f"=Son {cantidad} churros de {churro[0][1]} con un valor de ${total}=")
            print("=Ingrese una tecla para continuar=")
            msvcrt.getch()
            conexion.commit()
    except ValueError:
        print("=Error, ingrese el volor correcto en donde se le solicita=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
#-------------------------------------Registrar venta del pedido-------------------------------
def VentaDelPedido(pedidoID):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Pedidos")
        pedidos = cursor.fetchall()
        if not pedidos:
        #Verifica si hay clientes registrados
            clear()
            print("=No hay Pedidos registrados=")
            print("=Ingrese una tecla para continuar=")
            msvcrt.getch()
            return
        else:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Pedidos WHERE ID = ?", (pedidoID,))
            pedido = cursor.fetchall()
            if not pedido:
                print("No hay pedidos disponibles con esa selección")
                print("=Ingrese una tecla para continuar=")
                msvcrt.getch()
            churroid = pedido[0][0]
            clienteid = pedido[0][3]
            cursor.execute("SELECT * FROM Churros WHERE ID = ?", (churroid,))
            churro = cursor.fetchall()
            pcio = churro[0][2]
            fecha_actual = datetime.now()
            cursor.execute("""
                INSERT INTO VentasPP(ID_Churros, Precio, Fecha, ID_Clientes, ID_Pedidos) VALUES ( ?, ?, ?, ?, ?)""",
                (churroid, pcio, fecha_actual, clienteid, pedidoID))
            print("=Venta registrada con éxito!=")
            print("=Ingrese una tecla para continuar=")
            msvcrt.getch()
            conexion.commit()
    except ValueError as h:
        print(f"=Error {h}=")
        print("=Ingrese una tecla para continuar=")
        msvcrt.getch()
#Informe de Pedidos y Informe de Ventas "pendiente"
def registroVenta():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM VentasPP")
        VentaPP = cursor.fetchall()
        if not VentaPP:
        #Verifica si hay clientes registrados
            clear()
            print("=No hay Ventas por Pedido Registradas=")
            print("[Ingrese una tecla para continuar]")
            msvcrt.getch()
            return
        else:
            fichero = open('RegistroVentaXPedido.csv','a')
            for venta in VentaPP:
                fichero.write(f"(Numero de venta: {venta[0]},\nProducto: {venta[1]},\nTotal: {venta[2]},\nFecha: {venta[3]},\nCliente: {venta[4]},\nPedido N: {venta[5]})\n")

    except ValueError as h:
        print(f"=Error {h}=")
        print("[Ingrese una tecla para continuar]")
        msvcrt.getch() 
    
def registroVentana():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM VentasPV")
        VentaPV = cursor.fetchall()
        if not VentaPV:
        #Verifica si hay clientes registrados
            clear()
            print("=No hay Ventas por Ventana registradas=")
            print("[Ingrese una tecla para continuar]")
            msvcrt.getch()
            return
        else:
            fichero = open('RegistroVentaXLocal.csv','a')
            for venta in VentaPV:
                fichero.write(f"(Numero de venta: {venta[0]},\nProducto: {venta[1]},\nCantidad: {venta[2]},\nPrecio: {venta[3]},\nTotal: {venta[4]},\nFecha: {venta[5]})\n")
    except ValueError as h:
        print(f"=Error {h}=")
        print("[Ingrese una tecla para continuar]")
        msvcrt.getch() 
    
