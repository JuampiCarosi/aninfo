import random
from termcolor import colored
from validador import tiene_repeticiones, validar_rango_numero, sudoku_esta_lleno
import os

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

def elegir_dificultad():
    print("¡Bienvenido a Sudoku!")
    print("Para iniciar el juego, por favor elija la dificultad")
    print("1) Facil")
    print("2) Normal")
    print("3) Dificil")
    print("4) Salir\n")
    opcion = input("Ingrese la dificultad elegida: ")
    
    while(not validar_rango_numero(opcion, 1, 4)):
        opcion = input(", por favor, intenta de nuevo: ")

    if opcion == '1':
        print("\nHas seleccionado la dificultad Facil. A continuación se muestra el sudoku a resolver:\n")
        return "setsudokus/set_facil.txt"
    elif opcion == '2':
        print("\nHas seleccionado la dificultad Normal. A continuación se muestra el sudoku a resolver:\n")
        return "setsudokus/set_medio.txt"
    elif opcion == '3':
        print("\nHas seleccionado la dificultad Dificil. A continuación se muestra el sudoku a resolver:\n")
        return "setsudokus/set_dificil.txt"
    elif opcion == '4':
        print("\n¡Muchas gracias por jugar a Sudoku!")
        return None

def mostrar_tablero(tablero):
    i = 0
    print(colored("    1 2 3   4 5 6   7 8 9", 'blue'))
    for linea in tablero:
        print(colored(int(i/9 + 1), 'blue') + " | ", end="")
        for elemento in linea:
            if  (i%3 == 0) and (i != 0) and (i%9 != 0):
                print("| ", end = "")
            if elemento["editable"] :
                print(elemento["numero"], end= " ")
            else:
                print(colored(elemento["numero"],'red'), end= " ")
            i += 1
        if i in (27, 54):
            print("\n   " + "-" * 22)
        else:
            print("") 

def elegir_opcion_menu(sudoku):
    print("\n1) Ingresar número")
    print("2) Pedir una pista")
    print("3) Limpiar el tablero")
    print("4) Finalizar juego\n")
    opcion = input("Ingrese la opcion elegida: ")
    
    while(not validar_rango_numero(opcion, 1, 4)):
        opcion = input(", por favor, intenta de nuevo: ")
        
    if opcion == '1':
        agregar_numero(sudoku)
    elif opcion == '2':
        dar_pista(sudoku)
    elif opcion == '3':
        limpiar_tablero(sudoku)
    elif opcion == '4':
        finalizar(sudoku)
        return False
    return True

def agregar_numero(tablero):
    coordenada_ingresada = input("Ingrese una coordenada\n(debe ser un numero entre el 11 y el 99 donde el 1er numero es la fila y el 2do la columna): ")
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

def dar_pista(tablero):
    global pistas_restantes
    if pistas_restantes <= 0:
        print("No quedan pistas disponibles.")
        return
    
    if tiene_repeticiones(tablero):
        pistas_restantes -= 1
    else:
        print("El sudoku no tiene repeticiones.")
    
    print(f"Pistas restantes: {pistas_restantes}\n")

def limpiar_tablero(tablero):
    for linea in tablero:
        for celda in linea:
            if celda['editable']:
                celda['numero'] = '?'

def finalizar(sudoku):
    if not tiene_repeticiones(sudoku) and sudoku_esta_lleno(sudoku):
        print("¡Felicitaciones! Has completado el sudoku correctamente.\n")
    else:
        print("¡Lo sentimos! El sudoku es incorrecto.\n")
    print("¡Muchas gracias por jugar a Sudoku!")

def main():
    clear = lambda: os.system('cls')
    clear()
    ruta_archivo_set = elegir_dificultad()
    if ruta_archivo_set == None:
        return
    sudoku = creador_tablero(ruta_archivo_set)
    condicion = True
    while(condicion):
        mostrar_tablero(sudoku)
        condicion = elegir_opcion_menu(sudoku)

if __name__ == "__main__":
    main()