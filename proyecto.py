import random
import sys
from termcolor import colored, cprint

ruta_archivo_set = "setsudokus.txt"
pistas_restantes = 3


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


def aniadir_numero(tablero):
    coordenada_ingresada = input(
        "Ingrese una coordenada\n(debe ser un numero entre el 11 y el 99 donde el 1er numero es la fila y el 2do la columna): ")
    numero_ingresado = input("Ingrese un numero entre el 1 y el 9: ")
    if (len(coordenada_ingresada) == 2 and coordenada_ingresada[0].isdigit() and coordenada_ingresada[1].isdigit() and int(coordenada_ingresada[0]) > 0 and int(coordenada_ingresada[1]) > 0):
        # El -1 es porque la coordenada de la posicion 1x1 en la matriz es la posicion 0x0.
        fila = int(coordenada_ingresada[0]) - 1
        columna = int(coordenada_ingresada[1]) - 1
        if (numero_ingresado.isdigit() and len(numero_ingresado) == 1 and int(numero_ingresado) > 0):
            if tablero[fila][columna]['editable']:
                tablero[fila][columna]['numero'] = numero_ingresado
            else:
                print('\nLa coordenada ' +
                      coordenada_ingresada[0] + 'x' + coordenada_ingresada[1] + ' no puede ser modificada.')
        else:
            print('\nEl numero ingresado ' +
                  numero_ingresado + ' no es un numero valido.')
    else:
        print('\nLa coordenada ' + coordenada_ingresada +
              ' no es una coordenada valida.')


def mostrar_tablero(tablero):
    i = 0
    for linea in tablero:
        for elemento in linea:
            if (i % 3 == 0) and (i != 0) and (i % 9 != 0):
                print("|  ", end="")
            if elemento["editable"]:
                print(elemento["numero"], end="  ")
            else:
                print(colored(elemento["numero"], 'red'), end="  ")
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


def limpiar_tablero(tablero):
    for linea in tablero:
        for celda in linea:
            if celda['editable']:
                celda['numero'] = '?'


def dar_pista(tablero):
    global pistas_restantes
    if pistas_restantes <= 0:
        print("No quedan pistas disponibles.")
        return

    tiene_repeticiones = tiene_repeticiones(tablero)
    if tiene_repeticiones:
        print("Hay numeros incorrectos.")
    else:
        print("Todos los numeros ingresados son correctos.")
    pistas_restantes -= 1
