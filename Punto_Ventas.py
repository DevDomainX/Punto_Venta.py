#!/usr/bin/env python3
#Author: Hans saldias 
from colorama import init, Fore, Back, Style
import sqlite3 
import os
def crear_db():
    try:
        with sqlite3.connect("ventas.db") as con:
            cursor = con.cursor()
            cursor.execute('''CREATE TABLE if not exists                     productos
            (nombre VARCHAR(50), precio INTEGER)'''
            )
    except:
        print("Error")
    finally:
        print("Ahora solo ingrese productos")        
    
def agregar_productos():
    os.system("clear")
    print('''
88 88b 88  dP""b8 88""Yb 888888 .dP"Y8  dP"Yb    88""Yb
88 88Yb88 dP   `" 88__dP 88__   `Ybo." dP   Yb   88__dP
88 88 Y88 Yb  "88 88"Yb  88""   o.`Y8b Yb   dP   88°°°  .o.
88 88  Y8  YboodP 88  Yb 888888 8bodP'  YbodP    88     `"'
    ''')
    print("Agregando producto y  precio\n".upper())
    while True:
        with sqlite3.connect("ventas.db") as con:
            cursor = con.cursor()
            producto = input("Ingrese producto: ")
            precio = input("Ingrese precio: ")
            varios = [
            (producto, precio),]
            cursor.executemany("INSERT INTO productos                   VALUES(?, ?)", varios,
            )
            print("para menu escriba \"exit\" en producto y en precio")
            if producto == "exit":
                menu()
         
def ver_db():
    os.system("clear")
    print('''
             #        #            #
             #                     #
             #       ##     ###   ####    ###
             #        #    #       #         #
             #        #     ###    #      ####
             #        #        #   #  #  #   #
             #####   ###   ####     ##    ####
             ''')
    print("ver productos modo cadena\n".upper())
    with sqlite3.connect("ventas.db") as con:
         cursor = con.cursor()
         cursor.execute("SELECT * FROM  productos")
         print(cursor.fetchall())
             
         op = input("Ingrese 0 para volver al menu: ")      
         if op == "0":
             menu()
         else:
                 print("Opcion invalida")
    
    
        
def verlistado():
             os.system("clear")
             print('''
             #        #            #
             #                     #
             #       ##     ###   ####    ###
             #        #    #       #         #
             #        #     ###    #      ####
             #        #        #   #  #  #   #
             #####   ###   ####     ##    ####
             ''')
             print("ver productos modo lista\n".upper())
             with sqlite3.connect("ventas.db") as con:
                 cursor = con.cursor()
                 for fetchall in cursor.execute("SELECT * FROM                      productos"):
                         print(fetchall)
             
         
def fecha():
    os.system("clear")
    print('''
    888888 888888  dP""b8 88  88    db
    88__   88__   dP   `" 88  88   dPYb
    88""   88""   Yb      888888  dP__Yb
    88     888888  YboodP 88  88 dP""""Yb
    ''')
    print("Ingreso de nueva fecha\n".upper())
    with sqlite3.connect("ventas.db") as con:
            cursor = con.cursor()
            producto = input("Ingrese dia: ")
            precio = input("Ingrese fecha 00/00/00: ")
            varios = [
            (producto, precio),]
            cursor.executemany("INSERT INTO productos                   VALUES(?, ?)", varios,
            )
            
    
    
            
def menu():
    os.system("clear")
    while True:
       
       print(Fore.CYAN+Style.BRIGHT+'''
       8b    d8 888888 88b 88 88   88
       88b  d88 88__   88Yb88 88   88
       88YbdP88 88""   88 Y88 Y8   8P
       88 YY 88 888888 88  Y8 `YbodP'
    
        ''')
       print("=+="*22)
       print("Para iniciar elige opcion 1 para crear la base de                  datos de respaldo\n\nCreate by: Hans Saldias           ✓\n\n".upper())
       print("=+="*22)
       print("MENU VENTAS\n")
    
       print('''
        [1] crear Data Base para respaldo de los datos\n
        [2] Ingresar productos\n
        [3] ver modo continua Ingresados\n
        [4] ver como  modo lista\n
        [5] Ingresar nueva fecha ejem: fecha 25/05/23:\n
        '''.title())
       print("=+="*22)
       op = input("Ingrese opcion de menu: ")
       
        
       if op == "1":
           crear_db()
       elif op == "2":
           agregar_productos()
       elif op == "3":
           ver_db()
       elif op == "4":
           verlistado()
       elif op == "5":
           fecha()
       elif op == "salir":
           break
       else:
           print("Elija una opcion valida")
    
menu()    
       
    
   
    