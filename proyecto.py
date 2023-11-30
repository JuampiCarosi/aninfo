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
    nro_fila = 1
    coodenadas_bloqueadas = ()
    for caracter in caracteres:
        if caracter == '?':
            celda = {'numero': caracter, 'editable': True}
        else:
            celda = {'numero': caracter, 'editable': False}
        fila.append(celda)
        i += 1
        if caracter != '?':
            coordenada = str(nro_fila) + str(i)
            coodenadas_bloqueadas = coodenadas_bloqueadas + (coordenada,)
        if i == 9:
            tablero_final.append(fila)
            nro_fila += 1
            fila = []
            i = 0
    devolucion = []
    devolucion.append(tablero_final)
    devolucion.append(coodenadas_bloqueadas)
    return devolucion
