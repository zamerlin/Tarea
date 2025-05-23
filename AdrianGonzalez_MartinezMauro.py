import os
import msvcrt

def clear():
    #Definir una funcion para limpiar pantalla
    if os.name == "nt":
        #En este caso, se usa windows por lo que se ocupa el comando 'cls'
        os.system("cls")
    else:
        #de otra forma, al utilizarse linux se utilizaria el comando 'clear'
        os.system("clear")


def f_formaDePago(preciocondescton,formaDePago):
    #La forma de pago calcula el porcentaje a aplicar al precio
    if formaDePago == 1:
        descuento = -0.05
        cosa = "Efectivo"
        otro = "descuento de 5%"
    elif formaDePago == 2:
        descuento = 0.10
        cosa = "Tarjeta"
        otro = "aumento de 10%"
    elif formaDePago == 3:
        descuento = 0.15
        cosa = "Pagaré"
        otro = "aumento de 15%"
    else:
        print("Valor invalido")
        exit("Vuelva a intentarlo")
    descontando = preciocondescton * descuento
    #Se regresa con 'return' los valores llamados anteriormente
    return descontando, descuento, cosa, otro

def f_descuentoTonelada(subtotal,peso):
    #Al igual que el anterior, se calculan esta vez en base al peso solicitado
    if peso > 1:
        descton = 0.10
        prton = "10%"
    elif peso > 2:
        descton = 0.20
        prton = "20%"
    elif peso > 5:
        descton = 0.35
        prton = "35%"
    else:
        descton = 0.0
        prton = "0%"
    desctotal = subtotal * peso
    #Retorna el Valor tambien solicitado anteriormente
    return desctotal * descton, prton
        
def f_envio(kilometros):
    #Aqui regresa el valor que da en parentesis con una division entera
    #multiplicado por 50000 para saber el precio del envio por km
    return (kilometros // 100) * 50000

hojaverde = 36830
canchada = 139954
producto = " "
preciocondescton = 0
preciopago = 0
while True:
    try:
        #--------------------Inicio--------------------#
        print("***************************************")
        print("Calculadora del precio de la yerba mate")
        print("***************************************\n")

        #Definiendo tipos y asignando precio para mas adelante
        tipo = int(input("Ingrese el tipo de yerba:\n1_ Hoja verde\n2_ Canchada\n>>> "))
        if tipo == 1:
            producto = "Hoja Verde"
            total = hojaverde
        elif tipo==2:
            producto = "Canchada"
            total = canchada
        else:
            print("Valor no valido")
            exit("Vuelva a intentarlo")

        #Ingresando cantidad por toneladas para despues hacer los calculos
        peso = float(input("Ingrese el peso en toneladas de la yerba mate:\n>>> "))
        subtotal = total * peso
        desctonelada, porcentajetonelada = f_descuentoTonelada(total,peso)
        preciocondescton = subtotal - desctonelada


        #Definiendo formas de pago para calcular los descuentos
        formaDePago = int(input("Ingrese la forma de pago hecha:\n1_ Efectivo\n2_ Tarjeta\n3_ Pagaré\n>>> "))
        preccondesc, eldescuento, metododepago, parte = f_formaDePago(preciocondescton,formaDePago)
        #Final es con todo el ressto incluido
        preciopago = preciocondescton + preccondesc

        #Seccion de envios
        envio = str(input("Desea realizar un pedido de envio? S/N\n>>> "))
        envio = envio.upper()
        if envio == "S":
            kilometros = float(input("Ingrese a cuantos Km se encuentra del punto de venta\n>>> "))
            distancia = f_envio(kilometros)
            pfinal = preciopago + distancia
        
        #Impresion por pantalla de los resultados
        print(f"\nSu producto es de: {producto} con un precio unitario de ${total}")
        print(f"Llevando {peso} toneladas el precio es de ${subtotal}")
        print(f"Tambien llevando {peso} toneladas ud tiene {porcentajetonelada} (${desctonelada})de descuento que serian de: ${preciocondescton}")
        print(f"Usted cuenta con un {parte} {eldescuento:,.2f} pagando en {metododepago}")
        print(f"El subtotal es de ${preciopago} ")
        if envio == "S":
            print(f"El recargo por {kilometros} KM de envio es de {distancia}")
            print(f"Por lo que se le adicionara a un total de {pfinal}")
        else:
            print("Ud no solicito envio por lo que no tendrá recargos en ello")
            print(f"Por lo que su precio tiene un total de {preciopago}")

    except ValueError:
        print("Ingrese un valores correctos donde se le solicitan...")
        

    opc = str(input("Desea continuar? S/N\n>>>>> ")).upper()
    if opc == "S":
        pass
    elif opc == "N":
        break
    else:
        print("Opcion no valida")
        exit("Vuelva a intentarlo")

    clear()
print("Gracias por elegirnos!!!")