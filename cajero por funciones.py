#Simulador de cajero automatico de Martínez Mauro Gonzalo#
import os
import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

fondos=10000.0
def saldo(m):
    print("Su saldo de $", fondos)
    
def depositar(y,m):
    if depositoDinero <= 0:
        print("Ingrese solo numeros positivos enteros")
    elif depositoDinero > 0:
        fondos=fondos+depositoDinero
        print("Usted a ingresado $",depositoDinero," a su cuenta exitosamente, su saldo actual es de $",fondos)    

def retirar(z,m):
    if retiroDinero > fondos:
        print("Saldo Insuficiente para realizar esta transacción")
    elif retiroDinero <= fondos:
        fondos=fondos-retiroDinero
        print("Retiro de dinero exitoso, Usted a retirado $", retiroDinero, " de su cuenta, su saldo actual es de $",fondos)
    elif retiroDinero <=0:
        print("Ingrese solo numeros positivos enteros")

while True:    
    respuesta=str(input("===Cajero Automático===\n[1] Consultar su Saldo\n[2] Depositar Dinero\n[3] Retirar Dinero\n[4] Salir\n"))
    if respuesta == "1":
        saldo(fondos)
    elif respuesta == "2":
        while True:
            try:
                depositoDinero=int(input("Ingrese el monto a depositar\n"))
                depositar(depositoDinero)
                break 
            except:
                ValueError
                print("Ingrese solo numeros enteros")
    elif respuesta == "3":
        while True:
            try:
                retiroDinero=int(input("Ingrese el monto a retirar"))
                retirar(retiroDinero)
                break
            except:
                ValueError
                print("Ingrese solo numeros enteros")
    else:
        print("Opcion Incorrecta intente de Nuevo")
    
    print("[Precione una tecla para continuar]")
    msvcrt.getch()
    clear()