import random #Para poder seleccionar un tablero al azar

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
        fila.append(caracter)
        i += 1
        if i == 9:
            tablero_final.append(fila)
            fila = []
            i = 0
    return tablero_final