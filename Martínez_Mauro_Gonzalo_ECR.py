#Simulador de cajero automatico de Martínez Mauro Gonzalo#
import os
import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
fondos=10000.0

while True:    
    respuesta=str(input("===Cajero Automático===\n[1] Consultar su Saldo\n[2] Depositar Dinero\n[3] Retirar Dinero\n[4] Salir\n"))
    if respuesta == "1":
        print("Su saldo es de $", fondos)
    elif respuesta == "2":
        
        while True:
            depositoDinero=input("Ingrese el monto a depositar\n")
            if depositoDinero.isdigit():
                depositoDinero=int(depositoDinero)
                if depositoDinero <= 0:
                    print("Ingrese solo numeros positivos enteros")
                elif depositoDinero > 0:
                    fondos=fondos+depositoDinero
                    print("Usted a ingresado $",depositoDinero," a su cuenta exitosamente, su saldo actual es de $",fondos)
                    break            
            else:
                print("Ingrese solo numeros enteros")
    elif respuesta == "3":
        
        while True:
            retiroDinero=input("Ingrese el monto a retirar\n")
            if retiroDinero.isdigit():
                retiroDinero=int(retiroDinero)
                if retiroDinero > fondos:
                    print("Saldo Insuficiente para realizar esta transacción")
                elif retiroDinero <= fondos:
                    fondos=fondos-retiroDinero
                    print("Retiro de dinero exitoso, Usted a retirado $", retiroDinero, " de su cuenta, su saldo actual es de $",fondos)
                    break
                elif retiroDinero <=0:
                    print("Ingrese solo numeros positivos enteros")
            else:
                print("Ingrese solo numeros enteros")
    elif respuesta == "4":
        print("Usted esta saliendo del Sistema")
        break
    else:
        print("Opcion Incorrecta intente de Nuevo")
    
    print("[Precione una tecla para continuar]")
    msvcrt.getch()
    clear()