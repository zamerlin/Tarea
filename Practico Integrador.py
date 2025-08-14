import os
import msvcrt
import sqlite3

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

conexion= sqlite3.connect("baseDatos.db")
cursor = conexion.cursor()
print("Conexión exitosa.")

def descuento(a):
    descuento=a
    if descuento >=0:
        print()



