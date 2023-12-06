import random
import sys
from termcolor import colored, cprint

ruta_archivo_set = "setsudokus.txt"

def creador_tablero(ruta_archivo):
    archivo = open(ruta_archivo, 'r')
    set = archivo.readlines()
    nro_tablero_elegido = random.randint(0, len(set)-1)
    tablero_elegido = set[nro_tablero_elegido]
    caracteres = tablero_elegido.strip().split(',')
    tablero_final = []
    i = 0
    fila = []
    for caracter in caracteres:
        if caracter == '?':
            celda = {'numero': caracter, 'editable': True}
        else:
            celda = {'numero': caracter, 'editable': False}
        fila.append(celda)
        i += 1
        if i == 9:
            tablero_final.append(fila)
            fila = []
            i = 0
    return tablero_final

def mostrar_tablero(tablero):
    i = 0
    for linea in tablero:
        for elemento in linea:
            if  (i%3 == 0) and (i != 0) and (i%9 != 0):
                print("|  ", end = "")
            if elemento["editable"] :
                print(elemento["numero"], end= "  ")
            else:
                print(colored(elemento["numero"],'red'), end= "  ")
            i += 1
        if i in (27, 54):
            print("\n" + "-" * 31)
        else:
            print("\n") 

def es_opcion_valida(opcion):
    opcion_mayuc = opcion.upper()
    return opcion_mayuc == 'A' or opcion_mayuc == 'B' or opcion_mayuc == 'C' or opcion_mayuc == 'D'

def mostrar_menu():
    print("A) Ingresar número")
    print("B) Pedir una pista")
    print("C) Limpiar el tablero")
    print("D) Finalizar juego\n")

def pedir_opcion_a_realizar():
    opcion = input("Ingrese la opción a realizar: ")
    while not es_opcion_valida(opcion):
        print("La opción ingresada no es válida.")
        opcion = input("\nIngrese la opción a realizar: ")
    return opcion

