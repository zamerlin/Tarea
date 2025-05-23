#Original por Bernal y Duarte
#Archivo corregido y modificado por Adrian Gonzalez y Martínez Mauro

import os
import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def calcular_porcentaje(precio_total,descuento):   #Ingresamos el precio total de la compra que consta de:
    porcentaje = precio_total * (descuento/100)    #Tipo de yerba, toneladas y envío en caso de ser este último elegido.
    return porcentaje                              #Ingresamos los descuentos correspondientes
                                                   #y la función va a devolver la cantidad que debemos descontar.

def hacer_descuento(precio_total, descuento):  
    porcentaje = precio_total * (descuento / 100)  # Calculamos el valor del descuento  
    precio_final = precio_total - porcentaje       # Aplicamos el descuento  
    return precio_final                            #La función va a devolver el precio con los descuentos aplicados.

def aplicar_recargo(precio_total,recargo):         #Función para aplicar los recargos.
    recargo = precio_total * (recargo / 100)       # Calculamos el valor del descuento  
    precio_final = precio_total + recargo          # Aplicamos el descuento  
    return precio_final                            #solo que suma el porcentaje, aplicando así el recargo.

def asignar_descuento(cantidad):
    if  cantidad <=1:
        descuento = 0
        return descuento        
    elif cantidad > 1:
        descuento = 10
        return descuento
    elif cantidad > 2:
        descuento = 20
        return descuento
    elif cantidad > 5:
        descuento = 35 
        return descuento

def evaluar_tipoDato(valor):
    while True:
        try:
            valor = float(valor)
            if valor < 0:
                print("Cantidad inválida. Ingrese una cantidad superior a 0.")
                valor = input("Nueva cantidad: ")
                continue
            else:
                print("Espere, procesando...")
                return valor            

        except ValueError:
            print("Error. Ingrese un valor numérico.")
            valor = input("Ingrese una nueva cantidad: ")

def costo_envio(kilometros):

    recargo_por_100km = 50000
    recargo_km = kilometros

    if recargo_km > 0 and recargo_km < 100:
        recargo_km = 50000

    elif recargo_km >= 100:
        recargo_km = (kilometros / 100) * recargo_por_100km

    return recargo_km

def transaccion(contador, tipoYerba, cantidad, tipo, subtotal, descuento, envio, distancia, pago, precio_final):
    transaccionl = {'Tipo':tipoYerba,
                   'Cantidad':f"{tipo} Toneladas",
                   'Precio por tonelada':f"${subtotal}",
                   'Subtotal':f"${descuento}",
                   'Descuento/recargo':f"{cantidad}%",
                   'Envio':envio,
                   'Distancia':distancia,
                   'Forma de pago': pago,
                   'Precio final':f"${precio_final}"}
    transacciones[contador] = transaccionl
    transaccionl = False

def transaccion2(contador, tipoYerba,tipoYerbaDos, cantidad, cantidad2, tipo, tipoDos, subtotal, descuento, envio, distancia, pago, precioFinal):
    transaccionl = {'Tipo':tipoYerba,
                    'Tipo2':tipoYerbaDos,
                    'Cantidad':f"{cantidad} Toneladas",
                    'Cantidad2':f"{cantidad2} Toneladas",
                    'Precio por tonelada':f"${tipo}",
                    'Precio por tonelada2':f"${tipoDos}",
                    'Subtotal':f"${subtotal}",
                    'Descuento/recargo':f"{descuento}%",
                    'Envio':envio,
                    'Distancia':distancia,
                    'Forma de pago': pago,
                    'Precio final':f"${precioFinal}"}
    transacciones[contador] = transaccionl
    transaccionl = False
    
transacciones = {}    
contador = 0
tipo = 0
tipoYerba = ""
tipoDos = 0
tipoYerbaDos = ""

#---------------------------------------------Inicio---------------------------------------------------------------
while True:
        while True:
            print("=== Bienvenido a nuestro sistema de compra de Yerba Mate ===\nPor favor, ingrese su producto a adquirir:"
            "\n[1] Yerba mate hoja verde: $38.830,00\n[2] Yerba mate canchada: $139.954,00\n"
            "[3] Yerba mate saborizada: $47.000\n[4] Salir del Sistema")
        
            opcion = str(input(">>> "))
            if opcion == "1":
                tipoYerba = "Hoja Verde"
                tipo = 38830
                break
        
            elif opcion == "2":
                tipoYerba = "Canchada"
                tipo = 139954
                break
        
            elif opcion == "3":
                tipoYerba = "Saborizada"
                tipo = 47000
                break
        
            elif opcion == "4":
                exit("Gracias por elegir nuestros servicios. Vuelva pronto.")

            else:
                print("No se ingresó ninguna opción válida.")
        otro = str(input("Desea llevar algun otro producto más? \n[1] SI\n[2] No\n>>> "))
        clear()
        
        while True:
            
            if otro == "1":
                print("Por favor, ingrese su producto a adquirir:\n[1] Yerba mate hoja verde: $38.830,00\n[2] Yerba mate canchada: $139.954,00\n"
                "[3] Yerba mate saborizada: $47.000\n[4] Cancelar")
                opc = str(input(">>> "))
            
                if opc == "1":
                    tipoYerbaDos = "Hoja Verde"
                    tipoDos = 38830
                    break
        
                elif opc == "2":
                    tipoYerbaDos = "Canchada"
                    tipoDos = 139954
                    break
        
                elif opc == "3":
                    tipoYerbaDos = "Saborizada"
                    tipoDos = 47000
                    break
            
            elif otro == "2":
                break
            
            else:
                print("Opcion no válida, ingrese nuevamente")
        clear()
        print(f"Opcion 1 [{tipoYerba}] y Opcion 2 [{tipoYerbaDos}]")
#------------------------------------------Descuentos Cantidad----------------------------------------------------
        
        print("""Estos son los descuentos de nuestros productos\n
            Comprando más de 1 tonelada:  10% dto.
            Comprando más de 2 toneladas: 20% dto.
            Comprando más de 5 toneladas: 35% dto. """)
        cantidad = input(f"Ingrese la cantidad de toneladas de la yerba {tipoYerba} a comprar\n>>> ")
        print(f"Eligio {cantidad} Toneladas")
        cantidad = evaluar_tipoDato(cantidad)
        clear()
        
        if otro == "1":
            otracantidad = input(f"Ingrese la cantidad de toneladas de la yerba {tipoYerbaDos} a comprar\n>>> ")
            print(f"Eligio {cantidad} Toneladas")
            otracantidad = evaluar_tipoDato(otracantidad)
        
        clear()
        precio_total = tipo * cantidad    #usar funcion para calculo de descuentos
        
        if otro == "1":
            precio_totaldos = tipoDos * otracantidad
        descuento = asignar_descuento(cantidad)
        
        if otro == "1":
            descuentodos = asignar_descuento(otracantidad)
        #porcentaje = calcular_porcentaje(precio_total, descuento)
        precio_final = hacer_descuento(precio_total, descuento)
        
        if otro == "1":
            precio_finaldos = hacer_descuento(precio_totaldos, descuentodos)
        
        if otro == "1":
            print(f"El precio final de la yerba {tipoYerba} es de: $ {precio_final}\nY el precio final de la yerba {tipoYerbaDos} es de: $ {precio_finaldos}")
        
        else:
            print("El precio final es: $", precio_final)
        
        #-----------------------------------envio yerba-------------------------------------------------------------
        distancia = 0
        recargoTransporte = 0
        while True:
            envio= input("Desea que realicemos el envio (el envio no tiene descuentos) [1]Si o [2]No\n>>> ")
            
            if envio == "1":
        
                try:
                    distancia = int(input("\nIngrese la distancia en kilómetros para el envio\n>>> "))
                    recargoTransporte = costo_envio(distancia)
                    if otro == "1":
                        precio_final_def = recargoTransporte + precio_final + precio_finaldos
                    else:
                        precio_final_def = recargoTransporte + precio_final
                    print("El recargo por envios es de $50000, despues de los 100km aumentara otros 50000 cada 100Km.")
                    print(f"Su compra mas el envio da un total de ${precio_final_def}")
                    break
        
                except:
                    ValueError
                    print("Intente de nuevo") 
              
            elif envio == "2":
                    envio_no = "no"
                    print("Lo estaremos esperando para el retiro de su compra ^^")
                    break
            else:
                print("Valor Incorrecto")
        clear()        
    #---------------------------------------Metodo de pago yerba-----------------------------------------------------
        
        print("Formas de pago admitidas:\n[1] Efectivo: 5% de descuento adicional\n[2] Tarjeta de crédito: 10% de recargo \n[3] Pagaré: 15% de recargo")
        modo_pago = str(input("\nElija una de las opciones\n>>> "))
        clear()
        while True:
        
            if modo_pago == "1":
                descuento = 5
                pago = "Efectivo"
        
                if otro == "1":
                    subTotal = precio_final + precio_finaldos
                    precio_final1 = hacer_descuento(precio_final, descuento)
                    precio_finaldos = hacer_descuento(precio_finaldos, descuento)
                    precioFinal = precio_final1 + precio_finaldos + recargoTransporte
                    contador += 1
                    transaccion2(contador, tipoYerba, tipoYerbaDos, cantidad, otracantidad, tipo, tipoDos, subTotal, descuento, envio, distancia, pago, precioFinal)
        
                else:
                    subTotal = precio_final
                    precio_final1 = hacer_descuento(precio_final, descuento)
                    contador += 1
                    precioFinal= precio_final1 + recargoTransporte
                    transaccion(contador, tipoYerba, descuento, cantidad, tipo, subTotal, envio, distancia, pago, precioFinal)
                print(f"Estas fueron sus Transacciones {transacciones}")
                break
            
            elif modo_pago == '2':
                recargo = 10
                pago = "Tarjeta"
        
                if otro == "1":
                    subTotal = precio_final + precio_finaldos
                    precio_final1 = aplicar_recargo(precio_final, recargo)
                    precio_finaldos = aplicar_recargo(precio_finaldos, recargo)
                    precioFinal = precio_final1 + precio_finaldos + recargoTransporte
                    contador += 1
                    transaccion2(contador, tipoYerba, tipoYerbaDos, cantidad, otracantidad, tipo, tipoDos, subTotal, recargo, envio, distancia, pago, precioFinal)
        
                else:
                    contador += 1
                    subTotal = precio_final
                    precio_final1 = aplicar_recargo(precio_final, recargo)
                    precioFinal = precio_final1 + recargoTransporte
                    transaccion(contador, tipoYerba, recargo, cantidad, tipo, subTotal, envio, distancia, pago, precioFinal)
                print(f"Estas fueron sus Transacciones {transacciones}")
                break

            elif modo_pago == "3":
                recargo = 15
                pago = "Pagaré"
        
                if otro == "1":
                    subTotal = precio_final + precio_finaldos
                    precio_final1 = aplicar_recargo(precio_final, recargo)
                    precio_finaldos = aplicar_recargo(precio_finaldos, recargo)
                    precioFinal = precio_final1 + precio_finaldos + recargoTransporte
                    contador += 1
                    transaccion2(contador, tipoYerba, tipoYerbaDos, cantidad, otracantidad, tipo, tipoDos, subTotal, recargo, envio, distancia, pago, precioFinal)
        
                else:
                    contador += 1
                    subTotal = precio_final
                    precio_final1 = aplicar_recargo(precio_final, recargo)
                    precioFinal = precio_final1 + recargoTransporte
                    transaccion(contador, tipoYerba, recargo, cantidad, tipo, subTotal, envio, distancia, pago, precioFinal)
                print(f"Estas fueron sus Transacciones {transacciones}")
                break
            
            else:
                print("El dato introducido es invalido")        
        
        print("\n[Presione una tecla para continuar]")
        msvcrt.getch()
        clear()