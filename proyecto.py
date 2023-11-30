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

def mostrar_tablero(tablero):
    for fila in tablero:
        for celda in fila:
            print(celda['numero'], end=' ')
        print()

def mostrar_tablero_editable(tablero):
    for fila in tablero:
        for celda in fila:
            if celda['editable']:
                print(celda['numero'], end=' ')
            else:
                print('X', end=' ')
        print()

tablero = creador_tablero(ruta_archivo_set)
mostrar_tablero(tablero)
print()
mostrar_tablero_editable(tablero)