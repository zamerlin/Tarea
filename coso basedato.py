import sqlite3
import os
import msvcrt

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

conexion= sqlite3.connect("baseDatos.db")
cursor = conexion.cursor()
print("Conexión exitosa.")


cursor.execute('''CREATE TABLE IF NOT EXISTS agenda
(dni REAL PRIMARY KEY,
nombreApellido TEXT NOT NULL,
telefono REAL NOT NULL,
email TEXT NOT NULL,
direccion TEXT NOT NULL);''')
conexion.commit()

def subir():
    conexion.execute("INSERT INTO agenda (dni,nombreApellido,telefono,email,direccion) VALUES (?,?,?,?,?)",())
    conexion.commit()








while True:
    numero = input("[1] para agendar\n[2] para actualizar\n[3] para borrar \n[4] para ver todos los contactos\n[5]para salir\n>>>")
    if numero == "1":
        print("")
    elif numero == "2":
        print("")
    elif numero == "3":
        print("")
    elif numero == "4":
        print("")
    elif numero == "5":
        print("")
    break
    
    msvcrt.getch()
    clear()
conexion.close()