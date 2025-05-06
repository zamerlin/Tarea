#Simulador de cajero automatico, ahora con funciones de Martínez Mauro Gonzalo#

import os

import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

agenda = {}
<<<<<<< HEAD

fondos = 10000.0

contador = 0

def saldo(fondos):
    print("=Su saldo es de $", fondos, "=")
    
def depositar(fondos, contador, depositoDinero):
    titulo = "Depositar dinero"
    
    if depositoDinero > 0:
        fondos = fondos + depositoDinero
        print("=Usted a ingresado $", depositoDinero, "a su cuenta exitosamente=")
        print("=Su saldo actual es de $", fondos,"=")
        contador = contador
        agendar(fondos, contador, titulo, depositoDinero) 
        return fondos

def retirar(fondos, contador, retiroDinero):
    titulo = "Retirar Dinero"
    
    if retiroDinero <= fondos:
        fondos = fondos - retiroDinero
        print("=Retiro de dinero exitoso, Usted a retirado $", retiroDinero, " de su cuenta=")
        print("=Su saldo actual es de $",fondos,"=")
        contador = contador
        agendar(fondos, contador, titulo, retiroDinero)
        return fondos
    
def agendar(titulo, x, contador, fondos):
    #funcion de mierda no hace lo que quiero, pero quedo terminada#
    contadors = contador
    fondoss = fondos
    xs = x
    titulos = titulo
    agendar = {"Operacion" : contadors, "Fondos Actuales" : titulos, "fondos modificados" : fondoss}
    agenda[xs] = agendar
    agendar= False

=======

fondos = 10000.0

contador = 0

def saldo(fondos):
    print("=Su saldo es de $", fondos, "=")
    
def depositar(fondos, contador, depositoDinero):
    titulo = "Depositar dinero"
    
    if depositoDinero <= 0:
        print("=Ingrese solo numeros positivos enteros=")
    
    elif depositoDinero > 0:
        fondos = fondos + depositoDinero
        print("=Usted a ingresado $", depositoDinero, "a su cuenta exitosamente=")
        print("=Su saldo actual es de $", fondos,"=")
        contador = contador
        agendar(fondos, contador, titulo, depositoDinero) 
        return fondos

def retirar(fondos, contador, retiroDinero):
    titulo = "Retirar Dinero"
    
    if retiroDinero > fondos:
        print("=Saldo Insuficiente para realizar esta transacción=")
    
    elif retiroDinero <= fondos:
        fondos = fondos - retiroDinero
        print("=Retiro de dinero exitoso, Usted a retirado $", retiroDinero, " de su cuenta=")
        print("=Su saldo actual es de $",fondos,"=")
        contador = contador
        agendar(fondos, contador, titulo, retiroDinero)
        return fondos
    
def agendar(titulo, x, contador, fondos):
    #funcion de mierda no hace lo que quiero, pero quedo terminada#
    contadors=contador
    fondoss= fondos
    xs=x
    titulos=titulo
    agendar = {"ID":xs, "Fondos Actuales":titulos, "fondos modificados":fondoss}
    agenda[contadors] = agendar

>>>>>>> cabc8bcdad1136bac85e1e64157f033416cc3036

while True:
    print("===Cajero Automático===")
    respuesta= str (input("\n[1] Consultar su Saldo\n[2] Depositar Dinero\n[3] Retirar Dinero\n[4] Salir\n>>>"))
    
    if respuesta == "1":
        saldo(fondos)
    
    elif respuesta == "2":
        while True:
            try:
                depositoDinero = int(input("=Ingrese el monto a depositar=\n>>>"))
<<<<<<< HEAD
                if depositoDinero <= 0:
                     print("=Ingrese solo numeros positivos enteros=")
                else:     
                    contador += 1
                    fondos = depositar(fondos, contador, depositoDinero)
                    break 
=======
                contador += 1
                fondos = depositar(fondos, contador, depositoDinero)
                break 
>>>>>>> cabc8bcdad1136bac85e1e64157f033416cc3036
            except:
                ValueError
                print("=Ingrese solo numeros enteros=")
    
    elif respuesta == "3":
        while True:
            try:
                retiroDinero = int(input("=Ingrese el monto a retirar=\n>>>"))
<<<<<<< HEAD
                if retiroDinero > fondos:
                    print("=Saldo Insuficiente para realizar esta transacción=")
                else:
                    contador += 1
                    fondos = retirar(fondos, contador, retiroDinero)
                    break
=======
                contador += 1
                fondos = retirar(fondos, contador, retiroDinero)
                break
>>>>>>> cabc8bcdad1136bac85e1e64157f033416cc3036
            except:
                ValueError
                print("Ingrese solo numeros positivos enteros")
    
    elif respuesta == "5":
        print(agenda)
    
    else:
        print("=Opcion Incorrecta, intente de Nuevo=")
    
    print("[Precione una tecla para continuar]")
    msvcrt.getch()
    clear()