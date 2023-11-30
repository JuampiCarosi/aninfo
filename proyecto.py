import random

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

def aniadir_numero(coordenada_ingresada, numero_ingresado, tablero):
    fila = int(coordenada_ingresada[0]) - 1 #El -1 es porque la coordenada de la posicion 1x1 en la matriz es la posicion 0x0.
    columna = int(coordenada_ingresada[1]) - 1
    if tablero[fila][columna]['editable']:
        tablero[fila][columna]['numero'] = numero_ingresado
        print(tablero[fila][columna]['numero'])
    else:
        print('\nLa coordenada ' + coordenada_ingresada[0] + 'x' + coordenada_ingresada[1] + ' no puede ser modificada')
